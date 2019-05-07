import click

@click.group()
def clients():
    """Manges the clients lifecycles"""
    pass

@click.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    pass
 
@click.command()
@click.pass_context
def lista(ctx,):
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
