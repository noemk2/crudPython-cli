import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manges the clients lifecycles"""
    pass

@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service= ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@click.command()
@click.pass_context
def list(ctx,):
    """List all clients"""
    pass

@click.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a clients"""
    pass

@click.command()
@click.pass_context
def delete(ctx, client_uid):
    """Delete a new client """
    pass

all = clients
