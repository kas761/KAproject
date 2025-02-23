import click
from main import main

@click.command()
@click.option('--url_base', default='https://jsonplaceholder.typicode.com/', help='Base URL for the API')
@click.option('--data_type', type=click.Choice(['posts', 'comments', 'albums', 'photos', 'todos', 'users']), help='The type of data to process')

def cli(url_base, data_type):
    args = {'url_base': url_base, 'data_type': data_type}
    main(args)

if __name__ == '__main__':
    cli()