# Start build Dinner bot.

> reference : https://medium.com/@jacquelinewilson/amazon-alexa-skill-recipe-1444e6ee45a6


it probably takes 1~2hours to finish it.
Go to https://echosim.io and test it.
Amazon automatically will link between your AWS_lambda, Alexa.


## Tip for checking what libraries system has.
import sys<br/>
module = str(sys.modules.keys())<br/>
print(module)

> example : 
{
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'posix', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', '_bootlocale', '_locale', 'site', 'os', 'errno', 'stat', '_stat', 'posixpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', '_sysconfigdata_m_linux_x86_64-linux-gnu', 'pwd', '__future__', 'decimal', 'numbers', 'collections', 'operator', '_operator', 'keyword', 'heapq', '_heapq', 'itertools', 'reprlib', '_collections', '_decimal', 'imp', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'types', 'functools', '_functools', 'weakref', 'collections.abc', 'warnings', 'importlib.machinery', 'importlib.util', 'importlib.abc', 'contextlib', 'tokenize', 're', 'enum', 'sre_compile', '_sre', 'sre_parse', 'sre_constants', 'copyreg', 'token', 'json', 'json.decoder', 'json.scanner', '_json', 'json.encoder', 'logging', 'time', 'traceback', 'linecache', 'string', '_string', 'threading', 'atexit', 'socket', '_socket', 'selectors', 'math', 'select', 'runtime', 'wsgi', 'http', 'http.server', 'email', 'email.utils', 'random', 'hashlib', '_hashlib', '_blake2', '_sha3', 'bisect', '_bisect', '_random', 'datetime', '_datetime', 'urllib', 'urllib.parse', 'email._parseaddr', 'calendar', 'locale', 'email.charset', 'email.base64mime', 'base64', 'struct', '_struct', 'binascii', 'email.quoprimime', 'email.errors', 'email.encoders', 'quopri', 'html', 'html.entities', 'http.client', 'email.parser', 'email.feedparser', 'email._policybase', 'email.header', 'email.message', 'uu', 'email._encoded_words', 'email.iterators', 'ssl', 'ipaddress', 'textwrap', '_ssl', 'mimetypes', 'shutil', 'fnmatch', 'zlib', 'bz2', '_compression', '_bz2', 'lzma', '_lzma', 'grp', 'socketserver', 'copy', 'argparse', 'gettext', 'urllib.request', 'tempfile', 'urllib.error', 'urllib.response', 'wsgiref', 'wsgiref.simple_server', 'wsgiref.handlers', 'wsgiref.util', 'wsgiref.headers', 'platform', 'subprocess', 'signal', '_posixsubprocess', 'lambda_function'])"
    }
  }
}
