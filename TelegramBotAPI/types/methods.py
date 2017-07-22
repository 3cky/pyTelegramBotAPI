# -*- coding: utf-8 -*-

import json

from TelegramBotAPI.types.type import Type
from TelegramBotAPI.types.field import Field
from TelegramBotAPI.types.primitive import Integer, String, Boolean, Float, InputFile
from TelegramBotAPI.types.compound import ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, \
    InlineQueryResultArticle, InlineQueryResultGif, InlineQueryResultMpeg4Gif, \
    InlineQueryResultPhoto, InlineQueryResultVideo, InlineQueryResultGame, InlineKeyboardMarkup
from TelegramBotAPI.types.compound import Update, Message, User, UserProfilePhotos, File


class Method(Type):
    _response = None


class getUpdates(Method):
    _response = Update

    offset = Field(Integer, optional=True)
    limit = Field(Integer, optional=True)
    timeout = Field(Integer, optional=True)


class setWebhook(Method):
    url = Field(String)
    certificate = Field(InputFile, optional=True)


class getMe(Method):
    _response = User


class sendMessage(Method):
    _response = Message

    chat_id = Field(Integer, String)
    text = Field(String)
    parse_mode = Field(String, optional=True)
    disable_web_page_preview = Field(Boolean, optional=True)
    disable_notification = Field(Boolean, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)

    def _to_raw(self, strict=True):
        raw = super(sendMessage, self)._to_raw()
        if 'reply_markup' in raw:
            raw['reply_markup'] = json.dumps(raw['reply_markup'])
        return raw


class forwardMessage(Method):
    _response = Message

    chat_id = Field(Integer, String)
    from_chat_id = Field(Integer, String)
    message_id = Field(Integer)


class sendPhoto(Method):
    _response = Message

    chat_id = Field(Integer, String)
    photo = Field(InputFile, String)
    caption = Field(String, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendAudio(Method):
    _response = Message

    chat_id = Field(Integer, String)
    audio = Field(InputFile, String)
    duration = Field(Integer, optional=True)
    performer = Field(String, optional=True)
    title = Field(String, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendDocument(Method):
    _response = Message

    chat_id = Field(Integer, String)
    document = Field(InputFile, String)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendSticker(Method):
    _response = Message

    chat_id = Field(Integer, String)
    sticker = Field(InputFile, String)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendVideo(Method):
    _response = Message

    chat_id = Field(Integer, String)
    video = Field(InputFile, String)
    duration = Field(Integer, optional=True)
    caption = Field(String, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendVoice(Method):
    _response = Message

    chat_id = Field(Integer, String)
    audio = Field(InputFile, String)
    duration = Field(Integer, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendLocation(Method):
    _response = Message

    chat_id = Field(Integer, String)
    latitude = Field(Float)
    longitude = Field(Float)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, ReplyKeyboardMarkup,
                         ReplyKeyboardRemove, ForceReply, optional=True)


class sendChatAction(Method):
    _response = Boolean

    chat_id = Field(Integer, String)
    action = Field(String)


class sendGame(Method):
    _response = Message

    chat_id = Field(Integer)
    game_short_name = Field(String)
    disable_notification = Field(Boolean, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, optional=True)


class getUserProfilePhotos(Method):
    _response = UserProfilePhotos

    user_id = Field(Integer)
    offset = Field(Integer, optional=True)
    limit = Field(Integer, optional=True)


class getFile(Method):
    _response = File

    file_id = Field(String)


class answerInlineQuery(Method):
    _response = Boolean

    inline_query_id = Field(String)
    results = Field([InlineQueryResultArticle, InlineQueryResultGif, InlineQueryResultMpeg4Gif,
                     InlineQueryResultPhoto, InlineQueryResultVideo, InlineQueryResultGame])
    cache_time = Field(Integer, optional=True)
    is_personal = Field(Boolean, optional=True)
    next_offset = Field(String, optional=True)
    switch_pm_text = Field(String, optional=True)
    switch_pm_parameter = Field(String, optional=True)

    def _to_raw(self, strict=True):
        raw = super(answerInlineQuery, self)._to_raw()
        raw['results'] = json.dumps(raw['results'])
        return raw


class answerCallbackQuery(Method):
    _response = Boolean

    callback_query_id = Field(String)
    text = Field(String, optional=True)
    show_alert = Field(Boolean, optional=True)
    url = Field(String, optional=True)
    cache_time = Field(Integer, optional=True)


class editMessageText(Method):
    _response = Message

    chat_id = Field(Integer, String)
    message_id = Field(Integer, optional=True)
    inline_message_id = Field(String, optional=True)
    text = Field(String)
    parse_mode = Field(String, optional=True)
    disable_web_page_preview = Field(Boolean, optional=True)
    reply_markup = Field(InlineKeyboardMarkup, optional=True)

    def _to_raw(self, strict=True):
        raw = super(editMessageText, self)._to_raw()
        if 'reply_markup' in raw:
            raw['reply_markup'] = json.dumps(raw['reply_markup'])
        return raw
