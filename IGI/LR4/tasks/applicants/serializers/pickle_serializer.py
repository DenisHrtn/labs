import pickle


def save_to_pickle(applicants, filename='applicants.pkl'):
    with open(filename, 'wb') as pkl_file:
        pickle.dump(applicants, pkl_file)


def load_from_pickle(filename='applicants.pkl'):
    try:
        with open(filename, 'rb') as pkl_file:
            return pickle.load(pkl_file)
    except FileNotFoundError:
        print("Pickle file not found")
        return []
