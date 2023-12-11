import pickle


class BibTex_Repository():
    def __init__(self, connection):
        self._connection = connection

    def save(self, bibtex_obj, tag):
        cursor = self._connection.cursor()

        pickle_object = pickle.dumps(bibtex_obj)

        cursor.execute(
            '''INSERT INTO bibtex (citekey, data, tag) values (?,?,?)''',
            (bibtex_obj.citekey, pickle_object, tag)
        )

        self._connection.commit()

    def delete_object(self, citekey):
        cursor = self._connection.cursor()
        
        cursor.execute(
            """DELETE FROM bibtex WHERE citekey=?""",
            (citekey,)
        )
        rowcount = cursor.rowcount
        self._connection.commit()
        
        return rowcount != 0

    def find_reference(self, tag):
        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT * FROM bibtex WHERE tag=?""",
            (tag,)
        )
        result = cursor.fetchall()

        if result:
            result_list = [pickle.loads(res[1]) for res in result]
            return result_list
        return None

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute('''SELECT * FROM bibtex''')

        result = cursor.fetchall()

        result_list = []

        for row in result:
            unpickled = pickle.loads(row[1])
            result_list.append(unpickled)

        return result_list
