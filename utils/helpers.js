const SECRET_ENCRYPTION_KEY = 'GoldenToken'
const crypto = require('crypto');

export const encryptPassword = (password) => {
    return crypto.createHmac('md5', SECRET_ENCRYPTION_KEY)
        .update(password)
        .digest('hex')
        .toUpperCase();
};