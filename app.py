from flask import Flask, request, render_template
import pandas as pd
import io

app = Flask(__name__)

def process_uploaded_file(file_content):
    """
    Final version: Reads the "ALL BRANCH" Excel file and generates data for an enhanced dashboard with multiple views.
    """
    try:
        df = pd.read_excel(io.BytesIO(file_content), header=[2, 3])
    except Exception as e:
        raise ValueError(f"Could not read the Excel file. Error: {e}")

    # --- Header Flattening Logic ---
    new_columns = []
    for col in df.columns:
        top_header, sub_header = str(col[0]).strip(), str(col[1]).strip()
        if 'Unnamed:' in top_header:
            new_columns.append(sub_header.replace('Unnamed:', '').strip())
        elif 'Unnamed:' in sub_header:
            new_columns.append(top_header)
        else:
            new_columns.append(f"{top_header}_{sub_header}")
    df.columns = [col.replace('.', '').strip() for col in new_columns]

    # --- Data Cleaning & Type Conversion ---
    df.dropna(subset=['PART NUMBER'], inplace=True, how='all')

    stock_cols = [col for col in df.columns if 'STOCK' in col]
    sale_cols = [col for col in df.columns if 'SALE' in col and 'PERCENTAGE' not in col]
    
    # Ensure key columns exist before calculations
    for col in ['PERFORMANCE', 'AGEING', 'TRANSIT', 'PURCHASE']:
        if col not in df.columns:
            df[col] = 'N/A' if col == 'PERFORMANCE' else 0

    numeric_cols = ['PURCHASE', 'TRANSIT', 'AGEING'] + stock_cols + sale_cols
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
    df['TOTAL_STOCK'] = df[stock_cols].sum(axis=1)
    df['TOTAL_SALES'] = df[sale_cols].sum(axis=1)
    df['SALE %'] = (df['TOTAL_SALES'] / (df['TOTAL_STOCK'] + df['TOTAL_SALES'])).fillna(0)

    # --- Calculations for Dashboard Views ---
    
    # 1. KPIs
    total_products = len(df)
    purchase_qty = int(df['PURCHASE'].sum())
    sales_qty = int(df['TOTAL_SALES'].sum())
    stock_qty = int(df['TOTAL_STOCK'].sum())
    transit_qty = int(df['TRANSIT'].sum())
    avg_sales_percent = round(df['SALE %'].mean() * 100, 1) if not df['SALE %'].empty else 0
    low_stock_items = len(df[df['TOTAL_STOCK'] < 5])

    kpis = {
        "total_products": f"{total_products:,}", "purchase_qty": f"{purchase_qty:,}",
        "sales_qty": f"{sales_qty:,}", "stock_qty": f"{stock_qty:,}",
        "avg_sales_percent": avg_sales_percent, "low_stock_items": low_stock_items,
    }

    # 2. Inventory Status Chart
    inventory_status_chart = {
        'labels': ['Stock on Hand', 'In Transit'],
        'data': [stock_qty, transit_qty]
    }

    # 3. Performance Analysis Chart
    performance_counts = df['PERFORMANCE'].value_counts()
    performance_chart = {
        'labels': performance_counts.index.tolist(),
        'data': performance_counts.values.tolist()
    }
    
    # 4. Branch Chart (from before)
    branch_map = [
        {'name': 'APEX-JAFZA',   'stock': 'APEX-JAFZA_STOCK',   'sale': 'APEX - DEIRA_SALE'},
        {'name': 'APEX - DEIRA', 'stock': 'APEX - DEIRA_STOCK', 'sale': 'DUBAI_SALE'},
        {'name': 'DUBAI',        'stock': 'DUBAI_STOCK',        'sale': 'JEDDAH_SALE'},
        {'name': 'JEDDAH',       'stock': 'JEDDAH_STOCK',       'sale': 'RIYADH_SALE'},
        {'name': 'RIYADH',       'stock': 'RIYADH_STOCK',       'sale': 'DAMMAM_SALE'},
        {'name': 'DAMMAM',       'stock': 'DAMMAM_STOCK',       'sale': 'AXA SPARES_SALE'},
        {'name': 'AXA SPARES',   'stock': 'AXA SPARES_STOCK',   'sale': 'OMAN_SALE'},
        {'name': 'OMAN',         'stock': 'OMAN_STOCK',         'sale': 'SALALAH_SALE'},
        {'name': 'SALALAH',      'stock': 'SALALAH_STOCK',      'sale': 'BAHRAIN_SALE'},
        {'name': 'BAHRAIN',      'stock': 'BAHRAIN_STOCK',      'sale': 'TOTAL_SALE'},
    ]
    branch_chart = {
        'labels': [b['name'] for b in branch_map],
        'stock_data': [int(df[b['stock']].sum()) for b in branch_map],
        'sales_data': [int(df[b['sale']].sum()) for b in branch_map]
    }
    
    # 5. Category Chart (from before)
    df['Category'] = df['NAME'].apply(lambda x: 'Brake Shoe' if 'SHOE' in str(x).upper() else 'Brake Pad' if 'PAD' in str(x).upper() else 'Other')
    category_data_raw = df.groupby('Category')['TOTAL_STOCK'].sum()
    category_chart = {
        'labels': category_data_raw.index.tolist(),
        'data': [int(x) for x in category_data_raw.values.tolist()]
    }

    # 6. Top 10 Oldest Products Chart
    top_10_ageing = df.nlargest(10, 'AGEING')
    ageing_chart = {
        'labels': top_10_ageing['NAME'].tolist(),
        'data': [int(age) for age in top_10_ageing['AGEING'].tolist()]
    }

    # 7. Top 10 In-Transit Products Table
    top_10_transit = df.nlargest(10, 'TRANSIT')[['PART NUMBER', 'NAME', 'TRANSIT']].to_dict('records')

    # Combine all data into a single dictionary
    dashboard_data = {
        "kpis": kpis,
        "inventory_status_chart": inventory_status_chart,
        "performance_chart": performance_chart,
        "branch_chart": branch_chart,
        "category_chart": category_chart,
        "ageing_chart": ageing_chart,
        "top_10_transit": top_10_transit,
    }
    return dashboard_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error="No file part in the request.")
        
        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', error="No file selected for uploading.")

        # Check for allowed file types
        if file and (file.filename.endswith('.xlsx') or file.filename.endswith('.xls')):
            data, error = process_uploaded_file(file.stream)
            if error:
                 return render_template('index.html', error=error)
            return render_template('index.html', data=data)
        else:
            return render_template('index.html', error="Invalid file type. Please upload an Excel file (.xls, .xlsx).")

    # For a GET request, just show the page
    return render_template('index.html')


# --- Route for the AI Assistant Page ---
@app.route('/ai')
def ai_assistant():
    return render_template('ai_assistant.html')

# from flask import Flask, request, render_template
# import pandas as pd
# import io

# app = Flask(__name__)

# def process_uploaded_file(file_content):
#     """
#     Final version: This function is specifically tailored to the exact (and inconsistent)
#     column structure of the "ALL BRANCH" Excel file.
#     """
#     try:
#         # Read the Excel file, specifying that rows 3 and 4 (index 2 and 3) are the headers.
#         df = pd.read_excel(io.BytesIO(file_content), header=[2, 3])
#     except Exception as e:
#         raise ValueError(f"Could not read the Excel file. Error: {e}")

#     # --- Header Flattening Logic ---
#     new_columns = []
#     for col in df.columns:
#         top_header = str(col[0]).strip()
#         sub_header = str(col[1]).strip()
#         if 'Unnamed:' in top_header:
#             new_columns.append(sub_header.replace('Unnamed:','').strip())
#         elif 'Unnamed:' in sub_header:
#             new_columns.append(top_header)
#         else:
#             new_columns.append(f"{top_header}_{sub_header}")
#     df.columns = new_columns
#     df.columns = [col.replace('.','').strip() for col in df.columns]

#     # --- Data Cleaning & Type Conversion ---
#     df.dropna(subset=['PART NUMBER'], inplace=True, how='all')

#     stock_cols = [col for col in df.columns if 'STOCK' in col]
#     sale_cols = [col for col in df.columns if 'SALE' in col and 'PERCENTAGE' not in col]
    
#     if 'PERFORMANCE' not in df.columns:
#         df['PERFORMANCE'] = 'N/A'
        
#     numeric_cols = ['PURCHASE', 'TRANSIT'] + stock_cols + sale_cols

#     for col in numeric_cols:
#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
#     df['TOTAL_STOCK'] = df[stock_cols].sum(axis=1)
#     df['TOTAL_SALES'] = df[sale_cols].sum(axis=1)
#     df['SALE %'] = (df['TOTAL_SALES'] / (df['TOTAL_STOCK'] + df['TOTAL_SALES'])).fillna(0)

#     # --- Calculations ---
#     total_products = len(df)
#     purchase_qty = int(df['PURCHASE'].sum())
#     sales_qty = int(df['TOTAL_SALES'].sum())
#     stock_qty = int(df['TOTAL_STOCK'].sum())
#     avg_sales_percent = round(df['SALE %'].mean() * 100, 1) if not df['SALE %'].empty else 0
#     low_stock_items = len(df[df['TOTAL_STOCK'] < 5])

#     kpis = {
#         "total_products": f"{total_products:,}", "purchase_qty": f"{purchase_qty:,}",
#         "sales_qty": f"{sales_qty:,}", "stock_qty": f"{stock_qty:,}",
#         "avg_sales_percent": avg_sales_percent, "low_stock_items": low_stock_items,
#     }
    
#     # --- NEW: Hardcoded Map for Branch Chart ---
#     # This map correctly pairs branches to their misaligned stock and sale columns.
#     branch_map = [
#         {'name': 'APEX-JAFZA',   'stock': 'APEX-JAFZA_STOCK',   'sale': 'APEX - DEIRA_SALE'},
#         {'name': 'APEX - DEIRA', 'stock': 'APEX - DEIRA_STOCK', 'sale': 'DUBAI_SALE'},
#         {'name': 'DUBAI',        'stock': 'DUBAI_STOCK',        'sale': 'JEDDAH_SALE'},
#         {'name': 'JEDDAH',       'stock': 'JEDDAH_STOCK',       'sale': 'RIYADH_SALE'},
#         {'name': 'RIYADH',       'stock': 'RIYADH_STOCK',       'sale': 'DAMMAM_SALE'},
#         {'name': 'DAMMAM',       'stock': 'DAMMAM_STOCK',       'sale': 'AXA SPARES_SALE'},
#         {'name': 'AXA SPARES',   'stock': 'AXA SPARES_STOCK',   'sale': 'OMAN_SALE'},
#         {'name': 'OMAN',         'stock': 'OMAN_STOCK',         'sale': 'SALALAH_SALE'},
#         {'name': 'SALALAH',      'stock': 'SALALAH_STOCK',      'sale': 'BAHRAIN_SALE'},
#         {'name': 'BAHRAIN',      'stock': 'BAHRAIN_STOCK',      'sale': 'TOTAL_SALE'}, # Last column is also misaligned
#     ]

#     branch_labels = [b['name'] for b in branch_map]
#     branch_stock_data = [int(df[b['stock']].sum()) for b in branch_map]
#     branch_sales_data = [int(df[b['sale']].sum()) for b in branch_map]
    
#     branch_chart = { 'labels': branch_labels, 'stock_data': branch_stock_data, 'sales_data': branch_sales_data }
    
#     df['Category'] = df['NAME'].apply(lambda x: 'Brake Shoe' if 'SHOE' in str(x).upper() else 'Brake Pad' if 'PAD' in str(x).upper() else 'Other')
#     category_data_raw = df.groupby('Category')['TOTAL_STOCK'].sum()
#     category_chart = {
#         'labels': category_data_raw.index.tolist(),
#         'data': [int(x) for x in category_data_raw.values.tolist()]
#     }

#     display_df = df[['PART NUMBER', 'NAME', 'TOTAL_SALES', 'TOTAL_STOCK', 'SALE %', 'PERFORMANCE']]
#     display_df = display_df.rename(columns={'TOTAL_SALES': 'SALES', 'TOTAL_STOCK': 'STOCK'})
#     low_sales_df = display_df[display_df['SALE %'] < 0.1].sort_values(by='SALE %', ascending=True).head(10)

#     dashboard_data = {
#         "kpis": kpis, "branch_chart": branch_chart, "category_chart": category_chart,
#         "low_sales_products": low_sales_df.to_dict('records')
#     }
#     return dashboard_data

# @app.route('/', methods=['GET', 'POST'])
# def dashboard():
#     if request.method == 'POST':
#         if 'file' not in request.files: return "No file part", 400
#         file = request.files['file']
#         if file.filename == '': return "No selected file", 400
#         if file:
#             try:
#                 processed_data = process_uploaded_file(file.read())
#                 return render_template('index.html', data=processed_data)
#             except Exception as e:
#                 error_message = f"An error occurred: {e}"
#                 print(f"ERROR: {error_message}")
#                 return render_template('index.html', data=None, error=error_message)
#     return render_template('index.html', data=None)

# if __name__ == '__main__':
#     app.run(debug=True)