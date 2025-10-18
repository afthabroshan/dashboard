# # # # from flask import Flask, request, render_template
# # # # import pandas as pd
# # # # import io

# # # # app = Flask(__name__)

# # # # def process_uploaded_file(file_content):
# # # #     """
# # # #     Final version: Reads the "ALL BRANCH" Excel file and generates data for an enhanced dashboard with multiple views.
# # # #     """
# # # #     try:
# # # #         df = pd.read_excel(io.BytesIO(file_content), header=[2, 3])
# # # #     except Exception as e:
# # # #         raise ValueError(f"Could not read the Excel file. Error: {e}")

# # # #     # --- Header Flattening Logic ---
# # # #     new_columns = []
# # # #     for col in df.columns:
# # # #         top_header, sub_header = str(col[0]).strip(), str(col[1]).strip()
# # # #         if 'Unnamed:' in top_header:
# # # #             new_columns.append(sub_header.replace('Unnamed:', '').strip())
# # # #         elif 'Unnamed:' in sub_header:
# # # #             new_columns.append(top_header)
# # # #         else:
# # # #             new_columns.append(f"{top_header}_{sub_header}")
# # # #     df.columns = [col.replace('.', '').strip() for col in new_columns]

# # # #     # --- Data Cleaning & Type Conversion ---
# # # #     df.dropna(subset=['PART NUMBER'], inplace=True, how='all')

# # # #     stock_cols = [col for col in df.columns if 'STOCK' in col]
# # # #     sale_cols = [col for col in df.columns if 'SALE' in col and 'PERCENTAGE' not in col]
    
# # # #     # Ensure key columns exist before calculations
# # # #     for col in ['PERFORMANCE', 'AGEING', 'TRANSIT', 'PURCHASE']:
# # # #         if col not in df.columns:
# # # #             df[col] = 'N/A' if col == 'PERFORMANCE' else 0

# # # #     numeric_cols = ['PURCHASE', 'TRANSIT', 'AGEING'] + stock_cols + sale_cols
# # # #     for col in numeric_cols:
# # # #         df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
# # # #     df['TOTAL_STOCK'] = df[stock_cols].sum(axis=1)
# # # #     df['TOTAL_SALES'] = df[sale_cols].sum(axis=1)
# # # #     df['SALE %'] = (df['TOTAL_SALES'] / (df['TOTAL_STOCK'] + df['TOTAL_SALES'])).fillna(0)

# # # #     # --- Calculations for Dashboard Views ---
    
# # # #     # 1. KPIs
# # # #     total_products = len(df)
# # # #     purchase_qty = int(df['PURCHASE'].sum())
# # # #     sales_qty = int(df['TOTAL_SALES'].sum())
# # # #     stock_qty = int(df['TOTAL_STOCK'].sum())
# # # #     transit_qty = int(df['TRANSIT'].sum())
# # # #     avg_sales_percent = round(df['SALE %'].mean() * 100, 1) if not df['SALE %'].empty else 0
# # # #     low_stock_items = len(df[df['TOTAL_STOCK'] < 5])

# # # #     kpis = {
# # # #         "total_products": f"{total_products:,}", "purchase_qty": f"{purchase_qty:,}",
# # # #         "sales_qty": f"{sales_qty:,}", "stock_qty": f"{stock_qty:,}",
# # # #         "avg_sales_percent": avg_sales_percent, "low_stock_items": low_stock_items,
# # # #     }

# # # #     # 2. Inventory Status Chart
# # # #     inventory_status_chart = {
# # # #         'labels': ['Stock on Hand', 'In Transit'],
# # # #         'data': [stock_qty, transit_qty]
# # # #     }

# # # #     # 3. Performance Analysis Chart
# # # #     performance_counts = df['PERFORMANCE'].value_counts()
# # # #     performance_chart = {
# # # #         'labels': performance_counts.index.tolist(),
# # # #         'data': performance_counts.values.tolist()
# # # #     }
    
# # # #     # 4. Branch Chart (from before)
# # # #     branch_map = [
# # # #         {'name': 'APEX-JAFZA',   'stock': 'APEX-JAFZA_STOCK',   'sale': 'APEX - DEIRA_SALE'},
# # # #         {'name': 'APEX - DEIRA', 'stock': 'APEX - DEIRA_STOCK', 'sale': 'DUBAI_SALE'},
# # # #         {'name': 'DUBAI',        'stock': 'DUBAI_STOCK',        'sale': 'JEDDAH_SALE'},
# # # #         {'name': 'JEDDAH',       'stock': 'JEDDAH_STOCK',       'sale': 'RIYADH_SALE'},
# # # #         {'name': 'RIYADH',       'stock': 'RIYADH_STOCK',       'sale': 'DAMMAM_SALE'},
# # # #         {'name': 'DAMMAM',       'stock': 'DAMMAM_STOCK',       'sale': 'AXA SPARES_SALE'},
# # # #         {'name': 'AXA SPARES',   'stock': 'AXA SPARES_STOCK',   'sale': 'OMAN_SALE'},
# # # #         {'name': 'OMAN',         'stock': 'OMAN_STOCK',         'sale': 'SALALAH_SALE'},
# # # #         {'name': 'SALALAH',      'stock': 'SALALAH_STOCK',      'sale': 'BAHRAIN_SALE'},
# # # #         {'name': 'BAHRAIN',      'stock': 'BAHRAIN_STOCK',      'sale': 'TOTAL_SALE'},
# # # #     ]
# # # #     branch_chart = {
# # # #         'labels': [b['name'] for b in branch_map],
# # # #         'stock_data': [int(df[b['stock']].sum()) for b in branch_map],
# # # #         'sales_data': [int(df[b['sale']].sum()) for b in branch_map]
# # # #     }
    
# # # #     # 5. Category Chart (from before)
# # # #     df['Category'] = df['NAME'].apply(lambda x: 'Brake Shoe' if 'SHOE' in str(x).upper() else 'Brake Pad' if 'PAD' in str(x).upper() else 'Other')
# # # #     category_data_raw = df.groupby('Category')['TOTAL_STOCK'].sum()
# # # #     category_chart = {
# # # #         'labels': category_data_raw.index.tolist(),
# # # #         'data': [int(x) for x in category_data_raw.values.tolist()]
# # # #     }

# # # #     # 6. Top 10 Oldest Products Chart
# # # #     top_10_ageing = df.nlargest(10, 'AGEING')
# # # #     ageing_chart = {
# # # #         'labels': top_10_ageing['NAME'].tolist(),
# # # #         'data': [int(age) for age in top_10_ageing['AGEING'].tolist()]
# # # #     }

# # # #     # 7. Top 10 In-Transit Products Table
# # # #     top_10_transit = df.nlargest(10, 'TRANSIT')[['PART NUMBER', 'NAME', 'TRANSIT']].to_dict('records')

# # # #     # Combine all data into a single dictionary
# # # #     dashboard_data = {
# # # #         "kpis": kpis,
# # # #         "inventory_status_chart": inventory_status_chart,
# # # #         "performance_chart": performance_chart,
# # # #         "branch_chart": branch_chart,
# # # #         "category_chart": category_chart,
# # # #         "ageing_chart": ageing_chart,
# # # #         "top_10_transit": top_10_transit,
# # # #     }
# # # #     return dashboard_data

# # # # @app.route('/', methods=['GET', 'POST'])
# # # # def index():
# # # #     if request.method == 'POST':
# # # #         # Check if a file was uploaded
# # # #         if 'file' not in request.files:
# # # #             return render_template('index.html', error="No file part in the request.")
        
# # # #         file = request.files['file']

# # # #         # Check if the file is empty
# # # #         if file.filename == '':
# # # #             return render_template('index.html', error="No file selected for uploading.")

# # # #         # Check for allowed file types
# # # #         if file and (file.filename.endswith('.xlsx') or file.filename.endswith('.xls')):
# # # #             data, error = process_uploaded_file(file.stream)
# # # #             if error:
# # # #                  return render_template('index.html', error=error)
# # # #             return render_template('index.html', data=data)
# # # #         else:
# # # #             return render_template('index.html', error="Invalid file type. Please upload an Excel file (.xls, .xlsx).")

# # # #     # For a GET request, just show the page
# # # #     return render_template('index.html')


# # # # # --- Route for the AI Assistant Page ---
# # # # @app.route('/ai')
# # # # def ai_assistant():
# # # #     return render_template('ai_assistant.html')


# # # import requests
# # # from flask import Flask, render_template, jsonify

# # # # --- Configuration ---
# # # # Store your API details here for easy management.
# # # API_BASE_URL = "http://15.207.36.252/api/v3"
# # # AUTH_CLIENT = "12345"
# # # AUTH_TOKEN = "12345"
# # # ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjMzNjE4NDIsImlhdCI6MTc2MDc2OTg0Mn0.wrps4BuVab6zl9BCtsfYBIImyVoiVAmxznN_nCxCAZs"
# # # # IMPORTANT: Replace with your actual username and password for the API

# # # # --- Flask App Initialization ---
# # # app = Flask(__name__)



# # # @app.route('/')
# # # def show_sales_dashboard():
# # #     """
# # #     This route fetches the order data and displays it on a dashboard.
# # #     """
# # #     print("Fetching a new access token...")
# # #     access_token = ACCESS_TOKEN

# # #     print("Successfully obtained access token. Now fetching all orders...")

# # #     all_orders_url = f"{API_BASE_URL}/all_orders"
    
# # #     # Headers for the authenticated request
# # #     api_headers = {
# # #         "X-Auth-Client": AUTH_CLIENT,
# # #         "X-Auth-Token": AUTH_TOKEN,
# # #         "Authorization": f"Bearer {access_token}", # Use the token here
# # #         "Content-Type": "application/json"
# # #     }
    
# # #     # Payload for the all_orders request (as seen in Postman)
# # #     api_payload = {
# # #         "user_id": 25,
# # #         "page": 1,
# # #         "page_size": 100,
# # #         "orderDateFilterId": "",
# # #         "oderStatusId": ""
# # #     }
    
# # #     try:
# # #         response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
# # #         response.raise_for_status()
        
# # #         data = response.json()
        
# # #         # Check if the API call was successful internally
# # #         if data.get('result', {}).get('status') is True:
# # #             # Extract the list of orders from the nested JSON structure
# # #             orders_list = data['result']['delivery_details']['data']
            
# # #             # Pass the list of orders to the HTML template
# # #             return render_template('index.html', orders=orders_list)
# # #         else:
# # #             # Handle cases where the API returns a success HTTP code but an internal error
# # #             error_message = data.get('result', {}).get('message', 'Unknown API error')
# # #             return f"<h1>API Error: {error_message}</h1>", 500

# # #     except requests.exceptions.RequestException as e:
# # #         return f"<h1>Error fetching order data: {e}</h1>", 500


# # # if __name__ == '__main__':
# # #     # The 'debug=True' setting allows you to see errors in the browser
# # #     # and automatically reloads the server when you save changes.
# # #     app.run(debug=True)

# # import requests
# # import math # <-- Add this import at the top of your file
# # from flask import Flask, render_template

# # # --- Configuration (remains the same) ---
# # API_BASE_URL = "http://15.207.36.252/api/v3"
# # AUTH_CLIENT = "12345"
# # AUTH_TOKEN = "12345"
# # # NOTE: Using a hardcoded token will fail when it expires. 
# # # The function-based approach from the previous example is more robust.
# # ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjMzNjE4NDIsImlhdCI6MTc2MDc2OTg0Mn0.wrps4BuVab6zl9BCtsfYBIImyVoiVAmxznN_nCxCAZs"

# # # --- Flask App Initialization (remains the same) ---
# # app = Flask(__name__)

# # @app.route('/')
# # def show_sales_dashboard():
# #     """
# #     This route fetches ALL order data using pagination and displays it.
# #     """
# #     access_token = ACCESS_TOKEN
# #     all_orders_url = f"{API_BASE_URL}/all_orders"
    
# #     api_headers = {
# #         "X-Auth-Client": AUTH_CLIENT,
# #         "X-Auth-Token": AUTH_TOKEN,
# #         "Authorization": f"Bearer {access_token}",
# #         "Content-Type": "application/json"
# #     }
    
# #     page_size = 10 # Define page size once
# #     api_payload = {
# #         "user_id": 25,
# #         "page": 1,
# #         "page_size": page_size,
# #         "orderDateFilterId": "",
# #         "oderStatusId": ""
# #     }
    
# #     try:
# #         # --- Step 1: Make the first request ---
# #         print("Fetching page 1...")
# #         first_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
# #         first_response.raise_for_status()
# #         first_data = first_response.json()

# #         if not first_data.get('result', {}).get('status'):
# #             error_message = first_data.get('result', {}).get('message', 'Initial API error')
# #             return f"<h1>API Error: {error_message}</h1>", 500

# #         # --- Step 2: Initialize list and calculate total pages ---
# #         all_orders_list = first_data['result']['delivery_details']['data']
# #         total_items = first_data['result']['delivery_details']['totalItemCount']
# #         total_pages = math.ceil(total_items / page_size)
        
# #         print(f"Total items: {total_items}. Total pages: {total_pages}.")

# #         # --- Step 3: Loop through the rest of the pages (if any) ---
# #         if total_pages > 1:
# #             for page_num in range(2, total_pages + 1):
# #                 print(f"Fetching page {page_num}...")
# #                 api_payload['page'] = page_num # Update the page number in the payload
                
# #                 next_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
# #                 next_response.raise_for_status()
# #                 next_data = next_response.json()
                
# #                 if next_data.get('result', {}).get('status'):
# #                     # Add the new orders to our main list
# #                     all_orders_list.extend(next_data['result']['delivery_details']['data'])

# #         # --- Step 4: Render the template with the complete list ---
# #         return render_template('index.html', orders=all_orders_list)

# #     except requests.exceptions.RequestException as e:
# #         return f"<h1>Error fetching order data: {e}</h1>", 500

# # if __name__ == '__main__':
# #     app.run(debug=True)


# import requests
# import math
# from flask import Flask, render_template

# # --- Configuration ---
# API_BASE_URL = "http://15.207.36.252/api/v3"
# AUTH_CLIENT = "12345"
# AUTH_TOKEN = "12345"
# ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjMzNjE4NDIsImlhdCI6MTc2MDc2OTg0Mn0.wrps4BuVab6zl9BCtsfYBIImyVoiVAmxznN_nCxCAZs"

# # --- Flask App Initialization ---
# app = Flask(__name__)

# def process_dashboard_data(orders_list, total_items):
#     """
#     Processes the list of orders to calculate KPIs and chart data.
#     """
#     if not orders_list:
#         return {"kpis": {}, "sales_by_shop_chart": {"labels": [], "data": []}, "current_time": get_current_time()}

#     # --- 1. Calculate KPIs ---
#     total_sales_value = sum(order.get("totalPrice", 0) for order in orders_list)
#     unique_shops = len(set(order.get("shopName") for order in orders_list if order.get("shopName")))
#     avg_order_value = total_sales_value / len(orders_list) if orders_list else 0
    
#     kpis = {
#         "total_orders": f"{total_items:,}",
#         "total_sales": f"₹{total_sales_value:,.2f}",
#         "unique_shops": f"{unique_shops:,}",
#         "avg_order_value": f"₹{avg_order_value:,.2f}",
#     }

#     # --- 2. Prepare Data for Sales by Shop Chart ---
#     sales_by_shop = {}
#     for order in orders_list:
#         shop = order.get("shopName", "Unknown")
#         price = order.get("totalPrice", 0)
#         sales_by_shop[shop] = sales_by_shop.get(shop, 0) + price
    
#     sorted_shops = sorted(sales_by_shop.items(), key=lambda item: item[1], reverse=True)
    
#     sales_by_shop_chart = {
#         "labels": [shop[0] for shop in sorted_shops],
#         "data": [shop[1] for shop in sorted_shops]
#     }
    
#     return {
#         "kpis": kpis,
#         "sales_by_shop_chart": sales_by_shop_chart,
#         "current_time": get_current_time()
#     }

# def get_current_time():
#     """
#     Returns a static time based on the user's request for consistency.
#     This function is now cross-platform safe.
#     """
#     # Using static data as per the user request.
#     return {
#         "day_time": "Saturday, 2:36 PM",
#         "timezone": "IST",
#         "year": "2025"
#     }

# @app.route('/')
# def show_sales_dashboard():
#     """
#     Main route that fetches ALL order data using pagination, processes it,
#     and renders the dashboard.
#     """
#     access_token = ACCESS_TOKEN
#     all_orders_url = f"{API_BASE_URL}/all_orders"
    
#     api_headers = {
#         "X-Auth-Client": AUTH_CLIENT, "X-Auth-Token": AUTH_TOKEN,
#         "Authorization": f"Bearer {access_token}", "Content-Type": "application/json"
#     }
    
#     page_size = 100
#     api_payload = {
#         "user_id": 25, "page": 1, "page_size": page_size,
#         "orderDateFilterId": "", "oderStatusId": ""
#     }
    
#     try:
#         # Step 1: Make the first request
#         first_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
#         first_response.raise_for_status()
#         first_data = first_response.json()

#         if not first_data.get('result', {}).get('status'):
#             return "<h1>API Error: Could not fetch initial data.</h1>", 500

#         # Step 2: Initialize list and calculate total pages
#         all_orders_list = first_data['result']['delivery_details']['data']
#         total_items = first_data['result']['delivery_details']['totalItemCount']
#         total_pages = math.ceil(total_items / page_size)

#         # Step 3: Loop through the remaining pages
#         if total_pages > 1:
#             for page_num in range(2, total_pages + 1):
#                 api_payload['page'] = page_num
#                 next_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
#                 next_response.raise_for_status()
#                 next_data = next_response.json()
#                 if next_data.get('result', {}).get('status'):
#                     all_orders_list.extend(next_data['result']['delivery_details']['data'])

#         # Step 4: Process all the fetched data for the dashboard
#         dashboard_data = process_dashboard_data(all_orders_list, total_items)
        
#         # Step 5: Render the template
#         return render_template('index.html', 
#                                orders=all_orders_list,
#                                kpis=dashboard_data['kpis'],
#                                sales_chart_data=dashboard_data['sales_by_shop_chart'],
#                                current_time=dashboard_data['current_time'])

#     except requests.exceptions.RequestException as e:
#         return f"<h1>Error: Could not connect to the sales API. Details: {e}</h1>", 500

# if __name__ == '__main__':
#     app.run(debug=True)



import requests
import math
from flask import Flask, render_template

# --- Configuration ---


# -----API KEY INITIALIZING FOR .ENV----



# --- Flask App Initialization ---
app = Flask(__name__)

# --- Helper function to fetch all products (no changes needed here) ---
def get_all_products(headers):
    """
    Fetches all products from the API using pagination.
    """
    print("Fetching all products...")
    all_products_list = []
    page_num = 1
    page_size = 100
    
    while True:
        payload = {
            "user_id": 25, "page": page_num, "pageSize": page_size,
            "search_key": "", "brandId": ""
        }
        try:
            response = requests.post(f"{API_BASE_URL}/all_products", headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            if data.get('result', {}).get('status'):
                # --- THIS IS THE LINE TO FIX ---
                # OLD (unsafe): products_page = data['result']['product_details']['data']
                # NEW (safe):
                products_page = data['result'].get('product_details', {}).get('data', [])
                
                if not products_page:
                    # If the page returns no products, we've reached the end.
                    break 
                
                all_products_list.extend(products_page)
                page_num += 1 # Move to the next page for the next loop
            else:
                print("API returned a non-success status. Stopping.")
                break
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products on page {page_num}: {e}")
            break # Exit loop on error
            
    print(f"Finished fetching. Total products found: {len(all_products_list)}")
    return all_products_list
def group_products_by_brand(product_list):
    """
    Takes a flat list of products and returns a dictionary grouped by brand.
    """
    products_by_brand = {}
    for product in product_list:
        # Use the brand name as the key, or "Unbranded" if it's missing
        brand = product.get("brand") or "Unbranded"
        
        # If the brand is not yet a key in our dictionary, add it with an empty list
        if brand not in products_by_brand:
            products_by_brand[brand] = []
        
        # Append the current product to the list for its brand
        products_by_brand[brand].append(product)
        
    return products_by_brand
# --- Your existing dashboard helper functions (no changes) ---
def process_dashboard_data(orders_list, total_items):
    if not orders_list:
        return {"kpis": {}, "sales_by_shop_chart": {"labels": [], "data": []}, "current_time": get_current_time()}
    total_sales_value = sum(order.get("totalPrice", 0) for order in orders_list)
    unique_shops = len(set(order.get("shopName") for order in orders_list if order.get("shopName")))
    avg_order_value = total_sales_value / len(orders_list) if orders_list else 0
    kpis = {
        "total_orders": f"{total_items:,}",
        "total_sales": f"₹{total_sales_value:,.2f}",
        "unique_shops": f"{unique_shops:,}",
        "avg_order_value": f"₹{avg_order_value:,.2f}",
    }
    sales_by_shop = {}
    for order in orders_list:
        shop = order.get("shopName", "Unknown")
        price = order.get("totalPrice", 0)
        sales_by_shop[shop] = sales_by_shop.get(shop, 0) + price
    sorted_shops = sorted(sales_by_shop.items(), key=lambda item: item[1], reverse=True)
    sales_by_shop_chart = {
        "labels": [shop[0] for shop in sorted_shops],
        "data": [shop[1] for shop in sorted_shops]
    }
    return {
        "kpis": kpis,
        "sales_by_shop_chart": sales_by_shop_chart,
        "current_time": get_current_time()
    }

def get_current_time():
    return {
        "day_time": "Saturday, 4:07 PM",
        "timezone": "IST",
        "year": "2025"
    }

# --- Main Dashboard Route (UPDATED) ---
@app.route('/')
def show_sales_dashboard():
    access_token = ACCESS_TOKEN
    api_headers = {
        "X-Auth-Client": AUTH_CLIENT, "X-Auth-Token": AUTH_TOKEN,
        "Authorization": f"Bearer {access_token}", "Content-Type": "application/json"
    }
    
    try:
        # --- 1. Fetch Sales Order Data (no change) ---
        all_orders_list = []
        total_items = 0
        all_orders_url = f"{API_BASE_URL}/all_orders"
        page_size = 100
        api_payload = {
            "user_id": 25, "page": 1, "page_size": page_size,
            "orderDateFilterId": "", "oderStatusId": ""
        }
        first_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
        first_response.raise_for_status()
        first_data = first_response.json()

        if first_data.get('result', {}).get('status'):
            all_orders_list = first_data['result']['delivery_details']['data']
            total_items = first_data['result']['delivery_details']['totalItemCount']
            total_pages = math.ceil(total_items / page_size)

            if total_pages > 1:
                for page_num in range(2, total_pages + 1):
                    api_payload['page'] = page_num
                    next_response = requests.post(all_orders_url, headers=api_headers, json=api_payload)
                    next_data = next_response.json()
                    if next_data.get('result', {}).get('status'):
                        all_orders_list.extend(next_data['result']['delivery_details']['data'])
        
        dashboard_data = process_dashboard_data(all_orders_list, total_items)

        # --- 2. Fetch All Products Data (NEW) ---
        product_list = get_all_products(api_headers)
        products_by_brand = group_products_by_brand(product_list)
        # --- 3. Render Template with BOTH sets of data (UPDATED) ---
        return render_template('index.html', 
                               orders=all_orders_list,
                               kpis=dashboard_data['kpis'],
                               sales_chart_data=dashboard_data['sales_by_shop_chart'],
                               products_by_brand=products_by_brand,  # Pass the product list here
                               current_time=dashboard_data['current_time'])

    except requests.exceptions.RequestException as e:
        return f"<h1>Error: Could not connect to the sales API. Details: {e}</h1>", 500

if __name__ == '__main__':
    app.run(debug=True)