let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
	  \   'right': [['lineinfo'],
	  \				['percent'],
	  \				['fileformat', 'fileencoding', 'filetype']],
	  \   'left' : [['mode', 'paste'],
	  \		        ['gitbranch', 'readonly', 'filename', 'modified']]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'gitbranch#name'
      \ },
	  \ 'separator': { 'left': '', 'right': '' },
	  \ 'subseparator': { 'left': '', 'right': '' }
      \ }

" let g:lightline.colorscheme = 'PaperColor dark'
