import json
import os


TOKENS_PATH = os.path.join(os.getenv('HOME'), '.azure', 'accessTokens.json')


def token_(t):
    return {
        k: t[k] for k in
        ('resource', 'expiresOn', 'accessToken')
    }


def main():
    with open(TOKENS_PATH, 'r') as f:
        tokens = json.load(f)

    token_data = list(token_(t) for t in tokens)

    print(json.dumps(token_data, indent=2))
