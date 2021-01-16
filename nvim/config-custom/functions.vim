function! g:ToggleComment()
	normal! gv 

	let selection = [getpos("'<"), getpos("'>")]
	let endline = selection[1][1]
	let startline = selection[0][1]

	call VSCodeNotifyRange("editor.action.commentLine", startline, endline, 0)
	
endfunction
