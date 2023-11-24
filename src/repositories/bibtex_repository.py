import pickle


class BibTex_Repository():
    def __init__(self, connection):
        self._connection = connection

    def save(self, bibtex_obj):
        cursor = self._connection.cursor()

        pickle_object = pickle.dumps(bibtex_obj)

        cursor.execute(
            '''INSERT INTO bibtex (citekey, data) values (?,?)''',
            (bibtex_obj.citekey, pickle_object)
        )

        self._connection.commit()

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute('''SELECT * FROM bibtex''')

        result = cursor.fetchall()

        result_list = []

        for row in result:
            unpickled = pickle.loads(row[1])
            result_list.append(unpickled)

        return result_list
