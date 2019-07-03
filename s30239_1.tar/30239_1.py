from chimera import runCommand
cmds = [
    "",
    "",
    "open #0 pdb:1uw3_5.cryst",
    "",
    "open #1 pdb:3heq_6.cryst",
    "mmaker #0: #1: pair ss iter false",
    "",
    "open #2 pdb:3her_5.cryst",
    "mmaker #0: #2: pair ss iter false",
    "",
    "open #3 pdb:3hes_5.cryst",
    "mmaker #0: #3: pair ss iter false",
    "",
    "open #4 pdb:3o79_6.cryst",
    "mmaker #0: #4: pair ss iter false",
    "",
    "open #5 pdb:4hls_6.cryst",
    "mmaker #0: #5: pair ss iter false",
    "",
    "open #6 pdb:4hmm_6.cryst",
    "mmaker #0: #6: pair ss iter false",
    "",
    "open #7 pdb:4hmr_6.cryst",
    "mmaker #0: #7: pair ss iter false",
    "",
    "center #0",
    "",
    "",
    "rainbow",
]
for cmd in cmds:
    try:
        runCommand(cmd)
    except:
        pass
