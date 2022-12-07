Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import counter as c
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from collections import counter as c
ImportError: cannot import name 'counter' from 'collections' (C:\Users\HP\AppData\Local\Programs\Python\Python310\lib\collections\__init__.py)
from collections import Counter as c
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print(dict(c(sentence)))
{'t': 18, 'h': 9, 'e': 8, ' ': 26, 'c': 3, 'a': 15, 's': 2, 'o': 2, 'n': 6, 'm': 3, 'w': 4, 'i': 4, 'r': 4, 'd': 2, 'p': 3, 'l': 1, 'y': 2, 'g': 1}
counts = c(sentence)
print("\nType counts: ", type(counts))

Type counts:  <class 'collections.Counter'>
print(counts)
Counter({' ': 26, 't': 18, 'a': 15, 'h': 9, 'e': 8, 'n': 6, 'w': 4, 'i': 4, 'r': 4, 'c': 3, 'm': 3, 'p': 3, 's': 2, 'o': 2, 'd': 2, 'y': 2, 'l': 1, 'g': 1})
print("\n Occurrences of 'cat': ",counts['cat'])

 Occurrences of 'cat':  0
print("\n Occurrences of 'cat': ",counts['cat'])

 Occurrences of 'cat':  0


from datetime import datetime
KeyboardInterrupt
import time
dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
datetime.today()
datetime.datetime(2022, 12, 6, 8, 13, 39, 802072)
print(datetime.today())
2022-12-06 08:13:58.806045
datetime.now
<built-in method now of type object at 0x00007FFB98C38CD0>
datetime.now()
datetime.datetime(2022, 12, 6, 8, 15, 17, 276730)
print(datetime.now())
2022-12-06 08:15:45.711514
import sys
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
sys.path()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sys.path()
TypeError: 'list' object is not callable
sys.path
['', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin']
print(sys.path
KeyboardInterrupt
print(sys.path)
      
['', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin']
sys.exit
...       
<built-in function exit>
>>> sys.exit()
...       
>>> sys.exit(1)
...       
>>> dir(sys)
...       
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> sys.version
...       
'3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]'
>>> print(sys.version_info)
...       
sys.version_info(major=3, minor=10, micro=8, releaselevel='final', serial=0)
>>> print("sys.platform :",sys.platform)
...       
sys.platform : win32
