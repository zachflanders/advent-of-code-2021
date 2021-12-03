import pandas
import requests

from settings import cookie


class BinaryDiagnostic:

    def __init__(self):
        self.diagnostics = pandas.DataFrame(data=[
            [bit for bit in binary]
            for binary in requests.get(
                'https://adventofcode.com/2021/day/3/input',
                headers={'cookie': cookie}
            ).text.split('\n')[:-1]
        ])

    @property
    def gamma_rate(self):
        return int(''.join([
            self.diagnostics[column].mode().values[-1]
            for column in self.diagnostics.columns
        ]), 2)

    @property
    def epsilon_rate(self):
        return int(''.join([
            self._find_lead_common(self.diagnostics[column])
            for column in self.diagnostics.columns
        ]), 2)

    @property
    def o2_gen_rate(self):
        result = self.diagnostics.copy()
        for column in range(0, len(result.columns)):
            mode = result[column].mode().values[-1]
            result = result.loc[result[column] == mode]
        return int(''.join(result.iloc[0].to_list()), 2)

    @property
    def co2_scrub_rate(self):
        result = self.diagnostics.copy()
        for column in range(0, len(result.columns)):
            least_common = self._find_lead_common(result[column])
            result = result.loc[result[column] == least_common]
        return int(''.join(result.iloc[0].to_list()), 2)

    @staticmethod
    def _find_lead_common(series):
        value_counts = series.value_counts()
        if len(value_counts) > 1 and value_counts.to_list()[-1] == value_counts.to_list()[-2]:
            least_common = value_counts.index.to_list()[-2]
        else:
            least_common = value_counts.index.to_list()[-1]
        return least_common


if __name__ == '__main__':
    bd = BinaryDiagnostic()
    print(f'Solution 1: \
        gamma rate= {bd.gamma_rate} \
        epsilon rate = {bd.epsilon_rate} \
        product = {bd.gamma_rate * bd.epsilon_rate}')
    print(f'Solution 2: \
        oxygen generator rating = {bd.o2_gen_rate} \
        co2 scrub rating = {bd.co2_scrub_rate} \
        product = {bd.o2_gen_rate * bd.co2_scrub_rate}')
