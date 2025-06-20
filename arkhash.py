import hashlib
from urllib.parse import urlparse
import time

CLIENT_KEY = "gh67j345kl6hj5k432"

# very secure guys..
def generate_hash(url):
    pathname = urlparse(url).path
    intermediate_hash = hashlib.sha256(f"{pathname}:{str(int(time.time()))}:{CLIENT_KEY}".encode()).hexdigest()
    final_hash = hashlib.sha256(f"{CLIENT_KEY}:{intermediate_hash}".encode()).hexdigest()
    return final_hash
