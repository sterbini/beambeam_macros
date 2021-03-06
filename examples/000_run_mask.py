from cpymad.madx import Madx

beam = 1
i_octupoles = 100.
emittance_in_um = 2.3
n_particles = 2.25e11
chromaticity = 15
xing_angle_urad = 245.
seedran = 1

madx = Madx()
fname_mask = 'hl14_template.mask'

with open(fname_mask) as fid:
    mask_content = fid.read()

mask_content = mask_content.replace(r'%BEAM%', str(1))
mask_content = mask_content.replace(r'%OCT%', f'{i_octupoles:e}')
mask_content = mask_content.replace(r'%EMIT_BEAM', f'{emittance_in_um:e}')
mask_content = mask_content.replace(r'%NPART', f'{n_particles:e}')
mask_content = mask_content.replace(r'%CHROM%', f'{chromaticity:e}')
mask_content = mask_content.replace(r'%XING', f'{xing_angle_urad:e}')
mask_content = mask_content.replace(r'%SEEDRAN', f'{seedran:d}')

with open(fname_mask.split('.mask')[0]+'.unmask', 'w') as fid:
    fid.write(mask_content)

madx.input(mask_content)
