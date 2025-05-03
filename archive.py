import random

articles = [
    "https://www.enelgreenpower.com/it/learning-hub/transizione-energetica/cambiamento-climatico-cause-conseguenze",
    "https://www.wwf.it/cosa-facciamo/clima/cambiamenti-climatici/",
    "https://www.eon-energia.com/magazine/innovazione-e-ambiente/effetto-serra-cose-cause-e-conseguenze.html",
    "https://www.wwf.it/cosa-facciamo/clima/cambiamenti-climatici/",
    "https://tg24.sky.it/argomenti/cambiamento-climatico",
    "https://www.wwf.it/cosa-facciamo/mari-e-oceani/plastica/?psafe_param=1&utm_source=google&utm_medium=cpc_grant&utm_campaign=15024844931&ad_group=125590187261&match_type=&device=c&keyword=&utm_term=&gad_source=1&gbraid=0AAAAADvqmKKS1XV_9j40ajM96X3WEfCIZ&gclid=Cj0KCQjw_dbABhC5ARIsAAh2Z-T2Dr3DVDRPMUloMsXl9tSg09aZ8qoFQqkdhMUjNAjb-luXNpOb_C0aAlU_EALw_wcB#gad_source_1",
    "https://www.corriere.it/argomenti/cambiamento-climatico/",
    "https://www.wwf.ch/it/i-nostri-obiettivi/effetto-serra-come-i-gas-serra-cambiano-il-clima",
    "https://climate.ec.europa.eu/climate-change/consequences-climate-change_it",
    "https://www.humanitas.it/news/cambiamento-climatico-gli-effetti-sulla-salute/",
    "https://ambientenonsolo.com/il-rapporto-cina-2024-del-lancet-countdown-sulla-salute-e-i-cambiamenti-climatici-nel-colosso-asiatico/",
    "https://ambientenonsolo.com/il-rapporto-cina-2024-del-lancet-countdown-sulla-salute-e-i-cambiamenti-climatici-nel-colosso-asiatico/",
    "https://it.euronews.com/programmi/clima",
    "https://unric.org/it/effetti-del-cambiamento-climatico/",
    "https://www.repubblica.it/solidarieta/cooperazione/2022/11/18/news/oceania_dove_la_salute_del_pianeta_impatta_sulla_salute_umana_le_conseguenze_dellemergenza_climatica_sulla_salute_delle_pe-375123619/"
]

def random_article():
    return str(random.choice(articles))