import os
import win32com.client
import subprocess
import pypandoc

def convert_to_docx(directory):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file_path)
            output_file_path = os.path.join(root, f"{file_name}.docx")

            if file_extension.lower() in ['.odt', '.doc', '.docm', '.dot', '.dotm', '.html', '.pdf']:
                try:
                    if file_extension.lower() == '.odt':
                        subprocess.run(['unoconv', '-f', 'docx', file_path, '-o', output_file_path])
                    elif file_extension.lower() in ['.doc', '.docm', '.dot', '.dotm']:
                        doc = word.Documents.Open(file_path)
                        doc.SaveAs(output_file_path, FileFormat=16)  # 16 is the enum for .docx format
                        doc.Close()
                    elif file_extension.lower() in ['.html', '.pdf']:
                        pypandoc.convert_file(file_path, 'docx', outputfile=output_file_path)
                    
                    print(f"Converted {file_path} to {output_file_path}")
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to convert {file_path}: {e}")

    word.Quit()

# Diretório dos arquivos para converter e para salvar as conversões
directory = r'C:\Users\engwi\OneDrive\Documentos\Pasta compactada - peças DPE\Contestações'

convert_to_docx(directory)
