import database

# INSERT


def insert_photo(user_id, photo_url, caption, pet_type):
    database.sql_write("INSERT INTO photos (user_id, photo_url, caption, pet_type) VALUES(%s, %s, %s, %s);", [
                       user_id, photo_url, caption, pet_type])

# READ


def get_photo(photo_id):
    results = database.sql_select(
        "SELECT * FROM photos WHERE photo_id = %s;", [photo_id])
    result = results[0]
    return result

# READ_ALL


def get_all_photos(user_id):
    results = database.sql_select("SELECT photos.*, count(all_likes.user_id) as like_count, count(user_likes.user_id) as has_liked FROM photos " +
                                  "left join photo_likes all_likes on all_likes.photo_id=photos.photo_id " +
                                  "left join photo_likes user_likes on user_likes.photo_id=photos.photo_id and user_likes.user_id= %s GROUP BY photos.photo_id;", [user_id])
    return results


def get_all_Desc_most_popular(user_id):
    results = database.sql_select("SELECT photos.*, count(all_likes.user_id) as like_count, count(user_likes.user_id) as has_liked FROM photos " +
                                  "left join photo_likes all_likes on all_likes.photo_id=photos.photo_id " +
                                  "left join photo_likes user_likes on user_likes.photo_id=photos.photo_id and user_likes.user_id= %s GROUP BY photos.photo_id ORDER BY like_count DESC;", [user_id])
    return results


def get_photo_by_type(user_id, type):
    results = database.sql_select("SELECT photos.*, count(all_likes.user_id) as like_count, count(user_likes.user_id) as has_liked FROM photos " +
                                  "left join photo_likes all_likes on all_likes.photo_id=photos.photo_id " +
                                  "left join photo_likes user_likes on user_likes.photo_id=photos.photo_id and user_likes.user_id= %s WHERE photos.pet_type = %s GROUP BY photos.photo_id;", [user_id, type])
    return results
# UPDATE


def update_photos(photo_id, photo_url, caption, pet_type):
    database.sql_write("UPDATE photos SET photo_url= %s, caption = %s, pet_type=%s WHERE photo_id = %s;", [
        photo_url, caption, photo_id, pet_type])

# DELETE


def delete_photo(photo_id):
    database.sql_write("DELETE FROM photos WHERE photo_id = %s;", [photo_id])
