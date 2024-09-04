import openpyxl
import os.path as op

def save_file_modification(subject_id):
    #data_path = 'data path here' 
    subject_id_file_name = subject_id + '_emotional_faces_data.xlsx'
    save_file = op.join(data_path, subject_id_file_name)

    data_wb = openpyxl.Workbook() # opening the excel file now 

    #faces_strings = ['block_1', 'block_2', 'block_3'....]
    #variable_strings = [example: type of trial, arrow present?, actor, emotional face 1, emotional face 2]

    for ws_name in range(len(faces_strings)):
        data_wb.create_sheet(faces_strings[ws_name]) # creating a sheet to save each block 
        
        data_sheet = data_wb[faces_strings[ws_name]]
        
        for header in range(len(variable_strings)): # adding the headers
            data_sheet.cell(1, header+1, variable_strings[header])
    
    return data_wb, save_file
