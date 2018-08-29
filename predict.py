from lingpy import *
from lingrex.util import align_by_structure
from sys import argv
from lingrex.copar import CoPaR
from sys import argv

if 'clean' in argv:
    alms = Alignments('data/bodt-khobwa.csv', ref='crossids', fuzzy=True)
    ncid = max(alms.msa['crossids'])+1
    for idx, tks, struc, cogids in alms.iter_rows('tokens', 'structure', 'crossids'):
        if len(set(cogids)) != len(cogids):
            cogs = []
            for cid in cogids:
                if cid in cogs:
                    cogs += [ncid]
                    ncid += 1
                else:
                    cogs += [cid]
            alms[idx, 'crossids'] = basictypes.ints(cogs)
        
    align_by_structure(alms, segments='tokens', ref='crossids', structure='structure')
    
    D = {0: alms.columns}
    for idx in alms:
        D[idx] = [h for h in alms[idx]]
    wl = Wordlist(D)
    wl.output('tsv', filename='data/bodt-khobwa-cleaned', subset=True, 
            cols=['doculect', 'concept', 'value', 'form', 'tokens', 'structure', 'alignment',
                'crossids', 'morphemes', 'note'])

cp = CoPaR('data/bodt-khobwa-cleaned.tsv', ref='crossids', fuzzy=True)
# make function to extract correspondence patterns
cp.get_sites(minrefs=2, structure='structure')
cp.cluster_sites()
cp.sites_to_pattern()
cp.refine_patterns()

preds, purity, pudity = cp.predict_words()
goods = 0
with open('predictions.tsv', 'w') as f:
    f.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(
        'NUMBER', 'GOOD_PREDICTION', 'COGNATESET', 'LANGUAGE', 'CONCEPT', 'MORPHEME', 'WORD1',
        'WORD2', 'WORD3'
        ))
    num = 1
    for key, vals in sorted(preds.items(), key=lambda x: x[0]):
        # get the morphemes
        idx = cp.msa['crossids'][key]['ID'][0]
        cidx = cp[idx, 'crossids'].index(key)
        try:
            morph = cp[idx, 'morphemes'][cidx]
        except:
            morph = '?'
        for doc in vals:
            val1 = ' '.join([x.split('|')[0] for x in vals[doc]])
            if "Ø" in val1:
                no = '?'
            else:
                no = ''
                goods += 1
            val2 = ' '.join(['|'.join(x.split('|')[0:2]) for x in vals[doc]])
            val3 = ' '.join(vals[doc])

            f.write('\t'.join([str(num), no, str(key), doc, cp[idx, 'concept'],
                morph, val1, val2, val3])+'\n')
            num += 1
print('useful predictions', goods)
