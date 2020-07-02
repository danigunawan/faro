/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.TemplateList');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.FaceTemplate');

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
proto.TemplateList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.TemplateList.repeatedFields_, null);
};
goog.inherits(proto.TemplateList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.TemplateList.displayName = 'proto.TemplateList';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.TemplateList.repeatedFields_ = [1];



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
proto.TemplateList.prototype.toObject = function(opt_includeInstance) {
  return proto.TemplateList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.TemplateList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.TemplateList.toObject = function(includeInstance, msg) {
  var f, obj = {
    templatesList: jspb.Message.toObjectList(msg.getTemplatesList(),
    proto.FaceTemplate.toObject, includeInstance)
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
 * @return {!proto.TemplateList}
 */
proto.TemplateList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.TemplateList;
  return proto.TemplateList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.TemplateList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.TemplateList}
 */
proto.TemplateList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.FaceTemplate;
      reader.readMessage(value,proto.FaceTemplate.deserializeBinaryFromReader);
      msg.addTemplates(value);
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
proto.TemplateList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.TemplateList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.TemplateList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.TemplateList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getTemplatesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.FaceTemplate.serializeBinaryToWriter
    );
  }
};


/**
 * repeated FaceTemplate templates = 1;
 * @return {!Array<!proto.FaceTemplate>}
 */
proto.TemplateList.prototype.getTemplatesList = function() {
  return /** @type{!Array<!proto.FaceTemplate>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.FaceTemplate, 1));
};


/** @param {!Array<!proto.FaceTemplate>} value */
proto.TemplateList.prototype.setTemplatesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.FaceTemplate=} opt_value
 * @param {number=} opt_index
 * @return {!proto.FaceTemplate}
 */
proto.TemplateList.prototype.addTemplates = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.FaceTemplate, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 */
proto.TemplateList.prototype.clearTemplatesList = function() {
  this.setTemplatesList([]);
};


