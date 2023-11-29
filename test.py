from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-u', '--username', action='store', type=str, required=True)
parser.add_argument('-to', '--token', action='store', type=str, required=True)
parser.add_argument('-au', '--artifactory_url', action='store', type=str, default="https://jfrog.com/artifactory/", required=False)
parser.add_argument('-rj', '--recipe_json', action='store', type=str, required=True)
parser.add_argument('-dr', '--dryrun', action='store', type=str, default='False', required=False)
args = parser.parse_args()

print({'args': {'username': args.username, 'token': args.token, 'base_url': args.artifactory_url, 'recipe_json': args.recipe_json, 'dryrun': args.dryrun}}
)
