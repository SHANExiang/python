import pkg_resources


installed_packages = pkg_resources.working_set
installed_packages_list = sorted(
    ['%s==%s==%s' % (x.key, x.version, x.__dict__) for x in installed_packages])
for p in installed_packages_list:
    print(p)


# 类似如下打印
# aiocqhttp==1.2.3=={'project_name': 'aiocqhttp', '_version': '1.2.3',
# 'py_version': '3.8', 'platform': None,
# 'location': 'c:\\users\\administrator\\appdata\\local
# \\programs\\python\\python38\\lib\\site-packages',
# 'precedence': -1,
# '_provider': <pkg_resources.PathMetadata object at 0x000001524612A520>,
# '_key': 'aiocqhttp'}
