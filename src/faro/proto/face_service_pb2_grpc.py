# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from faro.proto import face_service_pb2 as faro_dot_proto_dot_face__service__pb2
from faro.proto import geometry_pb2 as faro_dot_proto_dot_geometry__pb2


class FaceRecognitionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.status = channel.unary_unary(
        '/FaceRecognition/status',
        request_serializer=faro_dot_proto_dot_face__service__pb2.FaceStatusRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceServiceInfo.FromString,
        )
    self.detect = channel.unary_unary(
        '/FaceRecognition/detect',
        request_serializer=faro_dot_proto_dot_face__service__pb2.DetectRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.extract = channel.unary_unary(
        '/FaceRecognition/extract',
        request_serializer=faro_dot_proto_dot_face__service__pb2.ExtractRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.score = channel.unary_unary(
        '/FaceRecognition/score',
        request_serializer=faro_dot_proto_dot_face__service__pb2.ScoreRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_geometry__pb2.Matrix.FromString,
        )
    self.enroll = channel.unary_unary(
        '/FaceRecognition/enroll',
        request_serializer=faro_dot_proto_dot_face__service__pb2.EnrollRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.search = channel.unary_unary(
        '/FaceRecognition/search',
        request_serializer=faro_dot_proto_dot_face__service__pb2.SearchRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.detectExtract = channel.unary_unary(
        '/FaceRecognition/detectExtract',
        request_serializer=faro_dot_proto_dot_face__service__pb2.DetectExtractRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.detectExtractEnroll = channel.unary_unary(
        '/FaceRecognition/detectExtractEnroll',
        request_serializer=faro_dot_proto_dot_face__service__pb2.DetectExtractEnrollRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.detectExtractSearch = channel.unary_unary(
        '/FaceRecognition/detectExtractSearch',
        request_serializer=faro_dot_proto_dot_face__service__pb2.DetectExtractSearchRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.galleryList = channel.unary_unary(
        '/FaceRecognition/galleryList',
        request_serializer=faro_dot_proto_dot_face__service__pb2.GalleryListRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.GalleryList.FromString,
        )
    self.galleryDelete = channel.unary_unary(
        '/FaceRecognition/galleryDelete',
        request_serializer=faro_dot_proto_dot_face__service__pb2.GalleryDeleteRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.Empty.FromString,
        )
    self.enrollmentList = channel.unary_unary(
        '/FaceRecognition/enrollmentList',
        request_serializer=faro_dot_proto_dot_face__service__pb2.EnrollmentListRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.enrollmentDelete = channel.unary_unary(
        '/FaceRecognition/enrollmentDelete',
        request_serializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.enrollmentDeleteConditional = channel.unary_unary(
        '/FaceRecognition/enrollmentDeleteConditional',
        request_serializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.enrollmentTransfer = channel.unary_unary(
        '/FaceRecognition/enrollmentTransfer',
        request_serializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.SerializeToString,
        response_deserializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.FromString,
        )
    self.echo = channel.unary_unary(
        '/FaceRecognition/echo',
        request_serializer=faro_dot_proto_dot_geometry__pb2.Matrix.SerializeToString,
        response_deserializer=faro_dot_proto_dot_geometry__pb2.Matrix.FromString,
        )


class FaceRecognitionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def status(self, request, context):
    """Service info and defaults
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def detect(self, request, context):
    """Simple operations
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def extract(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def score(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enroll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def detectExtract(self, request, context):
    """Combined opperations
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def detectExtractEnroll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def detectExtractSearch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def galleryList(self, request, context):
    """Gallery Management
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def galleryDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enrollmentList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enrollmentDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enrollmentDeleteConditional(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enrollmentTransfer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def echo(self, request, context):
    """Test
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FaceRecognitionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'status': grpc.unary_unary_rpc_method_handler(
          servicer.status,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.FaceStatusRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceServiceInfo.SerializeToString,
      ),
      'detect': grpc.unary_unary_rpc_method_handler(
          servicer.detect,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.DetectRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'extract': grpc.unary_unary_rpc_method_handler(
          servicer.extract,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.ExtractRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'score': grpc.unary_unary_rpc_method_handler(
          servicer.score,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.ScoreRequest.FromString,
          response_serializer=faro_dot_proto_dot_geometry__pb2.Matrix.SerializeToString,
      ),
      'enroll': grpc.unary_unary_rpc_method_handler(
          servicer.enroll,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.EnrollRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'search': grpc.unary_unary_rpc_method_handler(
          servicer.search,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.SearchRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'detectExtract': grpc.unary_unary_rpc_method_handler(
          servicer.detectExtract,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.DetectExtractRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'detectExtractEnroll': grpc.unary_unary_rpc_method_handler(
          servicer.detectExtractEnroll,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.DetectExtractEnrollRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'detectExtractSearch': grpc.unary_unary_rpc_method_handler(
          servicer.detectExtractSearch,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.DetectExtractSearchRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'galleryList': grpc.unary_unary_rpc_method_handler(
          servicer.galleryList,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.GalleryListRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.GalleryList.SerializeToString,
      ),
      'galleryDelete': grpc.unary_unary_rpc_method_handler(
          servicer.galleryDelete,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.GalleryDeleteRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.Empty.SerializeToString,
      ),
      'enrollmentList': grpc.unary_unary_rpc_method_handler(
          servicer.enrollmentList,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.EnrollmentListRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'enrollmentDelete': grpc.unary_unary_rpc_method_handler(
          servicer.enrollmentDelete,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'enrollmentDeleteConditional': grpc.unary_unary_rpc_method_handler(
          servicer.enrollmentDeleteConditional,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'enrollmentTransfer': grpc.unary_unary_rpc_method_handler(
          servicer.enrollmentTransfer,
          request_deserializer=faro_dot_proto_dot_face__service__pb2.EnrollmentDeleteRequest.FromString,
          response_serializer=faro_dot_proto_dot_face__service__pb2.FaceRecordList.SerializeToString,
      ),
      'echo': grpc.unary_unary_rpc_method_handler(
          servicer.echo,
          request_deserializer=faro_dot_proto_dot_geometry__pb2.Matrix.FromString,
          response_serializer=faro_dot_proto_dot_geometry__pb2.Matrix.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'FaceRecognition', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
