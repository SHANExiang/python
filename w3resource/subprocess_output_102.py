import subprocess


returned_text = subprocess.check_output('dir', shell=True,
                                        universal_newlines=True)
print(returned_text)
