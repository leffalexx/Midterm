import view as v
import model as m


def notebook_app():
    while True:
        match v.user_interface():
            case '1':
                m.add_note(v.new_note())
                v.confirmation()
            case '2':
                required_id = m.check_note(v.id_input())
                if required_id is not False:
                    v.show_note(m.get_note(required_id))
                else:
                    v.show_error()
            case '3':
                required_id = m.check_note(v.id_input())
                if required_id is not False:
                    m.edit_note(required_id, v.new_note())
                    v.confirmation()
                else:
                    v.show_error()
            case '4':
                required_id = m.check_note(v.id_input())
                if required_id is not False:
                    m.delete_note(required_id)
                    v.confirmation()
            case '5':
                content = m.read_file(m.file)
                for j in content:
                    v.show_note(j)
            case '6':
                list = m.get_by_date(v.get_date())
                for i in list:
                    v.show_note(i)
            case '7':
                break