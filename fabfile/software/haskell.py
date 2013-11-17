from fabric.api import task, sudo

@task
def ghc():
    sudo('pacman -Sy ghc')

@task
def cabal():
    sudo('pacman -Sy cabal-install')

@task
def all():
    '''
# haskell.all
ghc()
cabal()
    '''
    exec(all.__doc__)
