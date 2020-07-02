/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.EnrollRequest');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.EnrollOptions');
goog.require('proto.FaceRecordList');

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.EnrollRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.EnrollRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.EnrollRequest.displayName = 'proto.EnrollRequest';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.EnrollRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.EnrollRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.EnrollRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.EnrollRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    enrollGallery: jspb.Message.getFieldWithDefault(msg, 1, ""),
    records: (f = msg.getRecords()) && proto.FaceRecordList.toObject(includeInstance, f),
    enrollOptions: (f = msg.getEnrollOptions()) && proto.EnrollOptions.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.EnrollRequest}
 */
proto.EnrollRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.EnrollRequest;
  return proto.EnrollRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.EnrollRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.EnrollRequest}
 */
proto.EnrollRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setEnrollGallery(value);
      break;
    case 2:
      var value = new proto.FaceRecordList;
      reader.readMessage(value,proto.FaceRecordList.deserializeBinaryFromReader);
      msg.setRecords(value);
      break;
    case 10:
      var value = new proto.EnrollOptions;
      reader.readMessage(value,proto.EnrollOptions.deserializeBinaryFromReader);
      msg.setEnrollOptions(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.EnrollRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.EnrollRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.EnrollRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.EnrollRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnrollGallery();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getRecords();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      proto.FaceRecordList.serializeBinaryToWriter
    );
  }
  f = message.getEnrollOptions();
  if (f != null) {
    writer.writeMessage(
      10,
      f,
      proto.EnrollOptions.serializeBinaryToWriter
    );
  }
};


/**
 * optional string enroll_gallery = 1;
 * @return {string}
 */
proto.EnrollRequest.prototype.getEnrollGallery = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.EnrollRequest.prototype.setEnrollGallery = function(value) {
  jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional FaceRecordList records = 2;
 * @return {?proto.FaceRecordList}
 */
proto.EnrollRequest.prototype.getRecords = function() {
  return /** @type{?proto.FaceRecordList} */ (
    jspb.Message.getWrapperField(this, proto.FaceRecordList, 2));
};


/** @param {?proto.FaceRecordList|undefined} value */
proto.EnrollRequest.prototype.setRecords = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.EnrollRequest.prototype.clearRecords = function() {
  this.setRecords(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.EnrollRequest.prototype.hasRecords = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional EnrollOptions enroll_options = 10;
 * @return {?proto.EnrollOptions}
 */
proto.EnrollRequest.prototype.getEnrollOptions = function() {
  return /** @type{?proto.EnrollOptions} */ (
    jspb.Message.getWrapperField(this, proto.EnrollOptions, 10));
};


/** @param {?proto.EnrollOptions|undefined} value */
proto.EnrollRequest.prototype.setEnrollOptions = function(value) {
  jspb.Message.setWrapperField(this, 10, value);
};


/**
 * Clears the message field making it undefined.
 */
proto.EnrollRequest.prototype.clearEnrollOptions = function() {
  this.setEnrollOptions(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.EnrollRequest.prototype.hasEnrollOptions = function() {
  return jspb.Message.getField(this, 10) != null;
};


