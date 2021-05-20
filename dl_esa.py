import cdsapi
import numpy as np

c = cdsapi.Client()

year = YYEEAARR

c.retrieve(
    'satellite-sea-ice-concentration',
    {
        'version': 'v2',
        'variable': 'all',
        'format': 'zip',
        'month': [str(m).zfill(2) for m in np.arange(1, 12 + 1)],
        'year': str(year),
        'region': ['northern_hemisphere', 'southern_hemisphere'],
        'cdr_type': 'cdr',
        'origin': 'esa_cci',
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
    },
    'download_' + str(year) + '.zip')
