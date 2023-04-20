from paver.easy import task, cmdopts
from apps.common.commands.console.user_manager import create_admin_user
from apps.common.commands.tasks.exceptions import MissingOption


@task
@cmdopts([
    ('username=', 'u', 'Name of the user'),
    ('password=', 'p', 'Password of the user'),
    ('email=', 'e', 'Email of the user')
])
def create_admin(options):
    '''Create admin user'''
    try:
        for o in ('username', 'password', 'email'):
            if not hasattr(options, o):
                raise MissingOption(o)

        create_admin_user(
            username=options.username,
            password=options.password,
            email=options.email
        )

    except Exception as e:
        print(e)
    else:
        print('User admin created:')
        for o in ('username', 'password', 'email'):
            print(f"{o}: {getattr(options, o)}")
