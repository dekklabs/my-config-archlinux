" Source
source $HOME/.config/nvim/vim-plug/plugins.vim
source $HOME/.config/nvim/plug-config/coc.vim
source $HOME/.config/nvim/config-custom/mapping.vim
source $HOME/.config/nvim/config-custom/statusbarbottom.vim

" SET
:set cursorline
:set number
:set nocursorcolumn
:set tabstop=4
:set shiftwidth=4
" :syntax enable 
:set clipboard=unnamed
:syntax = enabled
:set showcmd
:set ruler
:set encoding=utf-8
:set showmatch
" :set sw=2
:set relativenumber
:set laststatus=2
:set noshowmode
:set laststatus=2
:set noshowmode
:set cmdheight=1
:set listchars=tab:··,trail:~,extends:>,precedes:<
:set list

" Color Column
hi Cursorline cterm=None ctermbg=8

" Let
let mapleader=" "
" let NERDTreeQuitOnOpen=1
let NERDTreeShowHidden=1

" Map
:map <C-n> :NERDTree
:map <Leader>s <Plug>(easymotion-s2)
:map <Leader>w :w<CR>
:map <Leader>q :q<CR>


" Export

" Functions
if !has('gui_running')
  set t_Co=256
endif
