# import sys
# import os
# from concurrent.futures import ThreadPoolExecutor

# def search_in_file(file_path, keyword):
#     results = []
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             for line_number, line in enumerate(file, start=1):
#                 if keyword.lower() in line.lower():
#                     results.append((line_number, line.strip()))
#     except Exception as e:
#         print(f"Error reading file {file_path}: {e}")
#     return file_path, results

# def search_in_files(folder_path, keyword, max_threads=4):
#     files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    
#     results = []
#     with ThreadPoolExecutor(max_threads) as executor:
#         futures = [executor.submit(search_in_file, file, keyword) for file in files]
#         for future in futures:
#             file_path, matches = future.result()
#             if matches:
#                 results.append((file_path, matches))
    
#     return results

# def main():
#     sys.stdout.reconfigure(encoding='utf-8')  # Set encoding to utf-8
    
#     folder_path = input("Enter the folder path containing text files: ")
#     keyword = input("Enter the keyword to search for: ")
    
#     if not os.path.exists(folder_path):
#         print("The folder does not exist. Please check the path.")
#         return
    
#     print("\nSearching... Please wait.")
#     results = search_in_files(folder_path, keyword)
    
#     if results:
#         print("\nSearch results found:")
#         for file_path, matches in results:
#             print(f"\nFile: {file_path}")
#             for line_number, line in matches:
#                 print(f"  Line {line_number}: {line}")
#     else:
#         print("\nNo results found.")

# if __name__ == "__main__":
#     main()


# import os
# from concurrent.futures import ThreadPoolExecutor
# from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END, WORD, ttk

# def search_in_file(file_path, keyword):
#     results = []
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             for line_number, line in enumerate(file, start=1):
#                 if keyword.lower() in line.lower():
#                     part = line.split('.')[0].split(',')[0]
#                     results.append((line_number, part.strip()))
#     except Exception as e:
#         print(f"Error reading file {file_path}: {e}")
#     return file_path, results

# def search_in_files(folder_path, keyword, max_threads=4):
#     files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
#     results = []
#     with ThreadPoolExecutor(max_threads) as executor:
#         futures = [executor.submit(search_in_file, file, keyword) for file in files]
#         for future in futures:
#             file_path, matches = future.result()
#             if matches:
#                 results.append((file_path, matches))
#     return results

# def highlight_keyword(text_widget, keyword):
#     start_index = "1.0"
#     while True:
#         start_index = text_widget.search(keyword, start_index, stopindex=END, nocase=True)
#         if not start_index:
#             break
#         end_index = f"{start_index}+{len(keyword)}c"
#         text_widget.tag_add("highlight", start_index, end_index)
#         start_index = end_index
#     text_widget.tag_config("highlight", background="yellow", foreground="black")

# def update_ui_progress(text_widget, message):
#     text_widget.insert(END, message + "\n")

# def search_and_display():
#     folder_path = folder_entry.get()
#     keyword = keyword_entry.get()
    
#     # Clear previous results
#     result_text.config(state='normal')
#     result_text.delete("1.0", END)
    
#     if not os.path.exists(folder_path):
#         update_ui_progress(result_text, "The folder does not exist. Please check the path.")
#         result_text.config(state='disabled')
#         return
    
#     update_ui_progress(result_text, "\nSearching... Please wait.")
#     results = search_in_files(folder_path, keyword)
    
#     if results:
#         update_ui_progress(result_text, "\nSearch results found:")
#         for file_path, matches in results:
#             update_ui_progress(result_text, f"\nFile: {file_path}")
#             for line_number, line in matches:
#                 update_ui_progress(result_text, f"  Line {line_number}: {line}")
#         highlight_keyword(result_text, keyword)
#     else:
#         update_ui_progress(result_text, "\nNo results found.")
    
#     result_text.config(state='disabled')

# # GUI setup
# root = Tk()
# root.title("Enhanced Search Tool")
# root.geometry("800x600")
# root.resizable(False, False)

# # Styling
# style = ttk.Style()
# style.theme_use('clam')  # Modern theme
# style.configure("TLabel", font=("Helvetica", 12), padding=5)
# style.configure("TEntry", font=("Helvetica", 12))
# style.configure("TButton", font=("Helvetica", 12), background="#4CAF50", foreground="white")

# # Frames
# top_frame = ttk.Frame(root, padding="10")
# top_frame.pack(fill='x', pady=10)

# middle_frame = ttk.Frame(root, padding="10")
# middle_frame.pack(fill='x', pady=10)

# bottom_frame = ttk.Frame(root, padding="10")
# bottom_frame.pack(fill='both', expand=True, pady=10)

# # Folder path input
# folder_label = ttk.Label(top_frame, text="Folder Path:")
# folder_label.pack(side="left", padx=5)

# folder_entry = ttk.Entry(top_frame, width=50)
# folder_entry.pack(side="left", padx=5)

# # Keyword input
# keyword_label = ttk.Label(middle_frame, text="Keyword:")
# keyword_label.pack(side="left", padx=5)

# keyword_entry = ttk.Entry(middle_frame, width=50)
# keyword_entry.pack(side="left", padx=5)

# # Search button
# search_button = ttk.Button(middle_frame, text="Search", command=search_and_display)
# search_button.pack(side="left", padx=5)

# # Results display
# result_text = Text(bottom_frame, wrap=WORD, font=("Helvetica", 12), bg="#F5F5F5")
# result_text.pack(side="left", fill='both', expand=True, padx=5)

# scrollbar = Scrollbar(bottom_frame, command=result_text.yview)
# scrollbar.pack(side="right", fill='y')
# result_text.config(yscrollcommand=scrollbar.set)

# # Run the application
# root.mainloop()



#  C:\Users\micheal.MICHOOL\Desktop\searchingTool.py
#  C:\Users\micheal.MICHOOL\Desktop\New folder (2)
# dependency

import os
from concurrent.futures import ThreadPoolExecutor
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END, WORD, ttk

def search_in_file(file_path, keyword):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if keyword.lower() in line.lower(): 
                    part = line.split('.')[0]
                    results.append((line_number, part.strip()))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return file_path, results

def search_in_files(folder_path, keyword, max_threads=1):
    # files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
    files = []
    for f in os.listdir(folder_path):
        if f.endswith('.txt'):
            files.append(os.path.join(folder_path, f))

    results = []
    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(search_in_file, file, keyword) for file in files] 
        
        for future in futures:
            file_path, matches = future.result()
            if matches:
                results.append((file_path, matches))
    return results

# Hello World Guys!
def highlight_keyword(text_widget, keyword):
    start_index = "1.0"
    # while True:
    #     start_index = text_widget.search(keyword, start_index, stopindex=END, nocase=True) # "1.6" or ""
    #     if not start_index: 
    #         break
    #     end_index = f"{start_index}+{len(keyword)}c"
    #     text_widget.tag_add("highlight", start_index, end_index)
    #     start_index = end_index
    # text_widget.tag_config("highlight", background="yellow", foreground="black")

def update_ui_progress(text_widget, message):
    text_widget.insert(END, message + "\n")

def search_and_display():
    folder_path = folder_entry.get()
    keyword = keyword_entry.get()
    
    # Clear previous results
    result_text.config(state='normal')
    result_text.delete("1.0", END)
    
    if not os.path.exists(folder_path):
        update_ui_progress(result_text, "The folder does not exist. Please check the path.")
        result_text.config(state='disabled')
        return
    
    update_ui_progress(result_text, "\nSearching... Please wait.")
    results = search_in_files(folder_path, keyword)
    
    if results:
        update_ui_progress(result_text, "\nSearch results found:")
        for file_path, matches in results:
            update_ui_progress(result_text, f"\nin File: {file_path}\n")
            for line_number, line in matches:
                update_ui_progress(result_text, f"  Line {line_number}: {line}")
        highlight_keyword(result_text, keyword)
    else:
        update_ui_progress(result_text, "\nNo results found.")
    
    result_text.config(state='disabled')

# GUI setup
root = Tk()
root.title("Enhanced Search Tool")
root.geometry("800x600")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use('clam')  # Modern theme
style.configure("TLabel", font=("Helvetica", 12), padding=5)
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), background="#4CAF50", foreground="white")

# Frames
top_frame = ttk.Frame(root, padding="10")
top_frame.pack(fill='x', pady=10)

middle_frame = ttk.Frame(root, padding="10")
middle_frame.pack(fill='x', pady=10)

bottom_frame = ttk.Frame(root, padding="10")
bottom_frame.pack(fill='both', expand=True, pady=10)

# Folder path input
folder_label = ttk.Label(top_frame, text="Folder Path:")
folder_label.pack(side="left", padx=5)

folder_entry = ttk.Entry(top_frame, width=50)
folder_entry.pack(side="left", padx=5)

# Keyword input
keyword_label = ttk.Label(middle_frame, text="Keyword:")
keyword_label.pack(side="left", padx=5)

keyword_entry = ttk.Entry(middle_frame, width=50)
keyword_entry.pack(side="left", padx=5)

# Search button
search_button = ttk.Button(middle_frame, text="Search", command=search_and_display)
search_button.pack(side="left", padx=5)

# Results display
result_text = Text(bottom_frame, wrap=WORD, font=("Helvetica", 12), bg="#F5F5F5")
result_text.pack(side="left", fill='both', expand=True, padx=5)

scrollbar = Scrollbar(bottom_frame, command=result_text.yview)
scrollbar.pack(side="right", fill='y')
result_text.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()

# Hello World -> 1.6 
# Mina farag ->1.5 + 0.5 = 1.10c

# Desktop\Mina -> Mina1.text -> mina nady, Mina2.text -> mina is a programmer, img.png
# Mina1.text
# Mina2.text

# import os
# from concurrent.futures import ThreadPoolExecutor

# def SearchInFile(filePath, keyword):
    
#     result = []
#     try:
#         with open(filePath, 'r', encoding='utf-8') as file:
#             for line_number, line in enumerate(file, start=1):
#                 if keyword in line:
#                     part = line.split('.')[0].split(',')[0]
#                     result.append((line_number, part))        
            
#     except Exception as e:
#         print(f"Error while reading file {filePath} : {e}.")
    
#     return filePath, result

# def SearchInFolder (folderPath, Keyword, threads = 4):
#     files = [os.path.join(folderPath, file) for file in os.listdir(folderPath) if file.endswith('.text')] #List Comprehension
    
#     result = []
#     with ThreadPoolExecutor(threads) as thread:
#         futures = [thread.submit(SearchInFile, file, Keyword) for file in files]
#         for future in futures:
#             file_path, line = future.result()
#             if line:
#                 result.append((file_path, line))
#     return result

# def higlightText (text_widget, keyword):
#     start_index = "1.0"
#     while True:
#         start_index = text_widget.search(keyword, start_index, stopindex = END, nocase = True) #"" or "1.6"
#         if not start_index:
#             break
#         end_index = f"{start_index} + {len(keyword)}c"
#         text_widget.tag_add("Highlight", start_index, end_index)
#         start_index = end_index
#         text_widget.tag_config("highlight", Background = "yellow", foreground = "black")