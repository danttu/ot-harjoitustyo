from invoke import task

@task
def start(ctx):
    ctx.run("python src/main.py", pty=False)