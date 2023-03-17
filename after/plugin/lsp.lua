local lsp = require('lsp-zero')

lsp.preset({
    name='recommended',
    set_lsp_keymaps = {omet = {'<F2>'}},
    manage_nvim_cmp = true,
    suggest_lsp_servers = false,
})

lsp.on_attach(function(client, bufnr)
    local opts = {buffer = bufnr}
    local bind = vim.keymap.set

    bind('n', '<leader>rn', '<cmd>lua vim.lsp.buf.rename()<cr>', opts)
end)

lsp.ensure_installed({
	'tsserver',
	'eslint',
	'lua_ls',
	'rust_analyzer',
	'pyright',
})

lsp.setup()
