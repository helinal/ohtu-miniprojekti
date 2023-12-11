import pickle
from rich import print  # pylint: disable=redefined-builtin
from services.IO import KonsoliIO


class BibTex_Repository():
    def __init__(self, connection):
        self._connection = connection
        self.io = KonsoliIO()

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
        status = ""  # pylint: disable=unused-variable
        try:
            cursor.execute(
                """DELETE FROM bibtex WHERE citekey=?""",
                (citekey,)
            )
            status = True
        except Exception as e:  # pylint: disable=unused-variable, W0718
            status = False

        self._connection.commit()
        # return status ongoing

    def find_reference(self, tag):
        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT * FROM bibtex WHERE tag=?""",
            (tag,)
        )
        result = cursor.fetchone()

        if result:
            result_list = []
            unpickled = pickle.loads(result[1])
            result_list.append(unpickled)
            self.io.print_readable_form(result_list)
        else:
            print("[bold red]\nCitekey not found.[bold red]")

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute('''SELECT * FROM bibtex''')

        result = cursor.fetchall()

        result_list = []

        for row in result:
            unpickled = pickle.loads(row[1])
            result_list.append(unpickled)

        return result_list
