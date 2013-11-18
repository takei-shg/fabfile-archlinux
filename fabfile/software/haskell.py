from fabric.api import task, sudo

@task
def ghc():
    sudo('pacman -Sy --noconfirm ghc')

@task
def cabal():
    sudo('pacman -Sy --noconfirm cabal-install')
    sudo('cabal update')
    sudo('cabal install cabal-install -j4 --prefix=/usr')

@task
def dev_tools():
    sudo('pacman -Sy --noconfirm happy')
    sudo('cabal update')
    sudo('cabal install haskell-src-exts ghc-mod stylish-haskell doctest -j4 --prefix=/usr')

@task
def all():
    '''
# haskell.all
ghc()
cabal()
dev_tools()
    '''
    exec(all.__doc__)
