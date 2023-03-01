from flask_restful import reqparse, abort, Api, Resource


def abort_if_user_not_found(user_id):
    from data import db_session
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, massage=f'User {user_id} not found')
    return user, session


class UsersResource(Resource):
    def get(self, user_id):
        user = abort_if_user_not_found(user_id)
        return jsonify({'user': user.to_dict(
            rules='jobs')})

    def delete(self, user_id):
        user, session = abort_if_user_not_found(user_id)
        session = db_session.create_session()
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session = session.query(User).all()
        return jsonify({'user':
            [item.to_dict(
                only=('id', 'name', 'surname', 'email', 'jobs.id', 'jobs.job'))
                for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(User).get(args.get('id'))
        if user:
            return jsonify({'error': 'Id already exists'})
        user = User(
            id=args.get['id'],
            surname=args['surname'],
            name=args['name'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'])
