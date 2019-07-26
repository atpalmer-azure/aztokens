import click
import json
import os


TOKENS_PATH = os.path.join(os.getenv('HOME'), '.azure', 'accessTokens.json')


def token_(t):
    return {
        k: t[k] for k in
        ('resource', 'expiresOn', 'accessToken')
    }


def get_resource_filter(resource_substr):
    if resource_substr is None:
        return lambda _: True
    def result(token):
        return resource_substr in token['resource']
    return result


@click.argument('resource', required=False)
@click.command()
def main(resource):
    with open(TOKENS_PATH, 'r') as f:
        tokens = json.load(f)

    is_match = get_resource_filter(resource)

    token_data = list(token_(t) for t in tokens if is_match(t))

    print(json.dumps(token_data, indent=2))
