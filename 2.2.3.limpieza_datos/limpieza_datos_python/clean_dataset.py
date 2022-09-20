import pandas as pd
import logging
import datetime as dt

def set_logging_configuration():
    """
    Returns the logger with the initial configurations, used for write log file.

        Parameters:
            None

        Returns:
            log (Logger): Logger object with the basic configuration.
    """
    FORMAT_LOG = '%(asctime)s %(section)s: %(message)s'
    logging.basicConfig(format=FORMAT_LOG, filename='logs/log_' + str(dt.date.today())+ '.log', encoding='utf-8')
    log = logging.getLogger('dev')
    log.setLevel(logging.DEBUG)
    return log


def get_normalize_data(dataset:pd.DataFrame, column_to_normalize:str, rules:dict) -> pd.DataFrame:
    """
    Returns a dataset with a column normalized, used defined rules.

        Parameters:
            dataset (DataFrame): DataFrame with datset's information.
            column_to_normalize (str): Name of column to normalize in the dataset
            rules (dict): A dictionary with normalize information, the form is {'rule_1': {'values': ['EUA', 'US', 'EE. UU'], 'norma': 'Estados Unidos'}}

        Returns:
            dataset (DataFrame): DataFrame with the normalized column.
    """
    if column_to_normalize == '' or len(rules) <= 0:
        raise ValueError("Column_to_normalize must be in the dataset and rules must be with the form {'rule_1': {'values': ['EUA', 'US', 'EE. UU'], 'norma': 'Estados Unidos'} }")
    for rule in rules:
        aux = dataset[column_to_normalize].apply(lambda value: rules[rule]['norma'] if value in rules[rule]['values'] else value)
        dataset[column_to_normalize] = aux
    return dataset


def get_treatment_of_null_values(dataset:pd.DataFrame) -> pd.DataFrame:
    """
    Returns dataset without null fields apply NaN.

        Parameters:
            dataset (DataFrame): DataFrame with datset's information.
        
        Returns:
            dataset (DataFrame): DataFrame with null fields to NaN. 
    """
    dataset = dataset.replace("", "NaN")
    return dataset


def decrease_dimensionality(dataset:pd.DataFrame, innecesary_colums:tuple) -> pd.DataFrame:
    """
        Returns a dataset without innesesary columns, reduces the matrix dimensionality.

            Parameters:
                dataset (DataFrame): DataFrame with datset's information.
                innecesary_colums (tuple): Tuple of strings, with name of innecesary colums.
            
            Returns:
                dataset (DataFrame): DataFrame without innecesary colums.
    """
    if len(innecesary_colums) <= 0:
        raise ValueError("In decrease_dimensionality is necesary the param innecesary_colums")
    for colum in innecesary_colums:
        dataset.pop(colum)
    return dataset


if __name__ == "__main__":
    log = set_logging_configuration()

    FILENAME = 'assets/Armas_Policias_Mexico'

    try:
        DATASET = pd.read_csv(FILENAME + '.csv')
        log.info('Dataset %s cargado correctamente.', FILENAME + '.csv', extra={'section': 'Main'})
    except FileNotFoundError as e:
        log.error('Dataset %s no encontrado, verifique si esta bien escrito.', FILENAME + '.csv', extra={'section': 'Main'})
        print(e)

    try:
        RULES = {'rule_1': {'values': ['EUA', 'US', 'EE. UU'], 'norma': 'Estados Unidos'}}
        clean_dataset = get_normalize_data(DATASET, 'Pais_origen_empresa', RULES)
        log.info('Dataset %s normalizado correctamente', FILENAME + '.csv', extra={'section': 'Main'})
    except ValueError as e:
        log.error('Verifique los parametros y la estructura: %s', e, extra={'section': 'get_normalize_data'})
        print(e)
    except TypeError as et:
        log.error('Verifique que los tipos de parametros: %s', e, extra={'section': 'get_normalize_data'})
        print(e)
    

    try:
        INNESESARY_COLUMNS = ('Usuario_agencia_estatal', 'Usuario_municipal?', 'Mes', 'Dia', 'Ano', 'Factura no.', 'Semi_auto_auto_n_a', 'Comentario')
        clean_dataset = decrease_dimensionality(DATASET, INNESESARY_COLUMNS)
        log.info('Dataset %s reducido correctamente', FILENAME + '.csv', extra={'section': 'Main'})
    except ValueError as e:
        log.error('Verifica el valor %s en "INNESESARY_COLUMNS"', e, extra={'section': 'decrease_dimensionality'})
        print('Error: ', e)
    
    clean_dataset.to_csv(FILENAME + '_clean.csv')
    log.info('Dataset %s limpio y creado correctamente', FILENAME + '.csv', extra={'section': 'Main'})