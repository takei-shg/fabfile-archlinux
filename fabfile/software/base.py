from fabric.api import task, sudo, run, cd, settings

@task
def package_query():
    with settings(warn_only=True):
      is_package_query_exist = sudo('pacman -Qs package-query')
    if is_package_query_exist.failed:
      sudo('pacman -Sy --noconfirm yajl')
      with cd('/usr/local/src'):
        sudo('wget https://aur.archlinux.org/packages/pa/package-query/package-query.tar.gz')
        sudo('tar xvzf package-query.tar.gz')
      with cd('/usr/local/src/package-query'):
        sudo('makepkg --asroot ; echo $?')
        sudo('pacman -U --noconfirm package-query-1.2-2-x86_64.pkg.tar.xz')

@task
def yaourt():
    with settings(warn_only=True):
      is_yaourt_exist = sudo('pacman -Qs yaourt')
    if is_yaourt_exist.failed:
      package_query()
      with cd('/usr/local/src'):
        sudo('wget https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz')
        sudo('tar xvzf yaourt.tar.gz')
      with cd('/usr/local/src/yaourt'):
        sudo('makepkg --asroot ; echo $?')
        sudo('pacman -U --noconfirm yaourt-1.3-1-any.pkg.tar.xz')

@task
def package():
    sudo('pacman -Sy --noconfirm base-devel tmux vim git tig zsh curl wget '
        'sqlite zip unzip')

# if package() fails, update the system
@task
def packageSyu():
    sudo('pacman -Syu --noconfirm base-devel tmux vim git tig zsh curl wget '
        'sqlite zip unzip')

@task
def nkf():
    sudo('yaourt -S --noconfirm nkf')

@task
def dotfiles():
    run('git clone --recursive git://github.com/daimatz/dotfiles')
    run('bash dotfiles/linker.sh')
    run('echo "source ~/.zsh/init.zsh" >> ~/.zshrc')
    sudo('chsh -s `which zsh` vagrant')

@task
def all():
    '''
# base.all
package()
yaourt()
nkf()
dotfiles()
    '''
    exec(all.__doc__)

@task
def all_withSysUpgrade():
    '''
# base.all_withSysUpgrade
packageSyu()
yaourt()
nkf()
dotfiles()
    '''
    exec(all_withSysUpgrade.__doc__)
