" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')
    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " Intellisence
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
	" Theme
	Plug 'morhetz/gruvbox'
	" Easymotion
    Plug 'easymotion/vim-easymotion'
	" Muestra estado de git en tree view
	Plug 'Xuyuanp/nerdtree-git-plugin'
	" Mejor vista del la barra inferior de estado
	Plug 'itchyny/lightline.vim'
	" Sintaxis JSX
	Plug 'maxmellon/vim-jsx-pretty'
	" Iconos de lenguajes
	Plug 'ryanoasis/vim-devicons'
	" Git branch
	Plug 'itchyny/vim-gitbranch'
	" Color highlight CSS
	Plug 'lilydjwg/colorizer'
	" Color verde a las carpetas e iconos
	Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
call plug#end()

" Tema
colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"

" Config easymotion
" let mapleader=" "
" nmap <Leader>s <Plug>(easymotion-s2)
