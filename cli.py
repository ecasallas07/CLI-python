import json_manager
import click


#decora la funcion
@click.group
def cli():
     pass
# cuando esta dentro de un group of commands debe ser @cli en vez de @click : https://click.palletsprojects.com/en/8.1.x/commands/
@cli.command(name='new_user')
@click.option('--name',required=True,help="user's name")
@click.option('--lastname',required=True,help="user's lastname")
@click.pass_context
def new(ctx,name,lastname):
     """Create a new register."""
     if not name or not lastname:
          ctx.fail('the name and lastname are required')
     else:
          data = json_manager.read_json()
          new_id = len(data) + 1
          new_register = { 'id': new_id, 'name': name, 'lastname': lastname}
          data.append(new_register)
          json_manager.write_json(data)
          print(f"new user created with  id {new_id}")


@cli.command(name='lis_users')
def users():
     data = json_manager.read_json()
     for user in data:
          print(f"{user['id']} - {user['name']} - {user['lastname']}")        
                         
@cli.comand(name='view_user')
@cli.argument('id',type=int)
def user(id):
     data = json_manager.read_json()     
     user =  next((x for x in data if x['id'] == id), None)
     if user is None:
          print("User not found")
     else:
          print(f"{user['id']} - {user['name']} - {user['lastname']}")
          
@cli.command()
@click.argument('id', type=int)
@click.option('--name', default=None)
@click.option('--lastname', default=None)
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print('user not found')
    else:
        data.remove(user)
        json_manager.write_json(data)     
     
# this form execute module main
if __name__ == '__main__':
    cli()