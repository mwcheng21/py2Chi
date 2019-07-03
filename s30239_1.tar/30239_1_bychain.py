from chimera import runCommand
cmds = [
    "",
    "",
    "open #0 pdb:1uw3_5.cryst",
    "",
    "open #1 pdb:3heq_6.cryst",
    "mmaker #0:.a #1:.a pair ss iter false",
    "",
    "open #2 pdb:3her_5.cryst",
    "mmaker #0:.a #2:.a pair ss iter false",
    "",
    "open #3 pdb:3hes_5.cryst",
    "mmaker #0:.a #3:.a pair ss iter false",
    "",
    "open #4 pdb:3o79_6.cryst",
    "mmaker #0:.a #4:.a pair ss iter false",
    "",
    "open #5 pdb:4hls_6.cryst",
    "mmaker #0:.a #5:.a pair ss iter false",
    "",
    "open #6 pdb:4hmm_6.cryst",
    "mmaker #0:.a #6:.a pair ss iter false",
    "",
    "open #7 pdb:4hmr_6.cryst",
    "mmaker #0:.a #7:.a pair ss iter false",
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
