import subprocess


# 执行一个命令将执行结果以一个字节字符串的形式返回，如果需要文本形式返回，加个解码操作即可。
out_bytes = subprocess.check_output(['netstat', '-a'])
text = out_bytes.decode()

# 如果被执行的命令以非零码返回，就会抛出异常
try:
    output_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    output_bytes = e.output
    code = e.returncode

# 默认情况下，check_output()仅仅返回输入到标准输出的值。如果你需要同时收集标准输出和错误输出，使用 stderr 参数
output_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'],
                                       stderr=subprocess.STDOUT)
# 如果你需要用一个超时机制来执行命令，使用 timeout 参数：
try:
    output_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    pass

# 如果你想让命令被一个 shell执行，传递一个字符串参数，并设置参数 shell=True
output_bytes = subprocess.check_output('grep python |wc > out', shell=True)
