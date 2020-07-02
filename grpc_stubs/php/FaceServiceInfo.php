<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faro/proto/face_service.proto

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>FaceServiceInfo</code>
 */
class FaceServiceInfo extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>.ServiceStatus status = 1;</code>
     */
    private $status = 0;
    /**
     * Generated from protobuf field <code>int32 worker_count = 2;</code>
     */
    private $worker_count = 0;
    /**
     * Generated from protobuf field <code>bool detection_support = 3;</code>
     */
    private $detection_support = false;
    /**
     * Generated from protobuf field <code>bool extract_support = 4;</code>
     */
    private $extract_support = false;
    /**
     * Generated from protobuf field <code>bool score_support = 5;</code>
     */
    private $score_support = false;
    /**
     * Generated from protobuf field <code>bool attribute_support = 6;</code>
     */
    private $attribute_support = false;
    /**
     * Generated from protobuf field <code>.ScoreType score_type = 7;</code>
     */
    private $score_type = 0;
    /**
     * Generated from protobuf field <code>float detection_threshold = 8;</code>
     */
    private $detection_threshold = 0.0;
    /**
     * Generated from protobuf field <code>float match_threshold = 9;</code>
     */
    private $match_threshold = 0.0;
    /**
     * Generated from protobuf field <code>string algorithm = 10;</code>
     */
    private $algorithm = '';
    /**
     * Generated from protobuf field <code>string notes = 11;</code>
     */
    private $notes = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type int $status
     *     @type int $worker_count
     *     @type bool $detection_support
     *     @type bool $extract_support
     *     @type bool $score_support
     *     @type bool $attribute_support
     *     @type int $score_type
     *     @type float $detection_threshold
     *     @type float $match_threshold
     *     @type string $algorithm
     *     @type string $notes
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Faro\Proto\FaceService::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>.ServiceStatus status = 1;</code>
     * @return int
     */
    public function getStatus()
    {
        return $this->status;
    }

    /**
     * Generated from protobuf field <code>.ServiceStatus status = 1;</code>
     * @param int $var
     * @return $this
     */
    public function setStatus($var)
    {
        GPBUtil::checkEnum($var, \ServiceStatus::class);
        $this->status = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>int32 worker_count = 2;</code>
     * @return int
     */
    public function getWorkerCount()
    {
        return $this->worker_count;
    }

    /**
     * Generated from protobuf field <code>int32 worker_count = 2;</code>
     * @param int $var
     * @return $this
     */
    public function setWorkerCount($var)
    {
        GPBUtil::checkInt32($var);
        $this->worker_count = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>bool detection_support = 3;</code>
     * @return bool
     */
    public function getDetectionSupport()
    {
        return $this->detection_support;
    }

    /**
     * Generated from protobuf field <code>bool detection_support = 3;</code>
     * @param bool $var
     * @return $this
     */
    public function setDetectionSupport($var)
    {
        GPBUtil::checkBool($var);
        $this->detection_support = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>bool extract_support = 4;</code>
     * @return bool
     */
    public function getExtractSupport()
    {
        return $this->extract_support;
    }

    /**
     * Generated from protobuf field <code>bool extract_support = 4;</code>
     * @param bool $var
     * @return $this
     */
    public function setExtractSupport($var)
    {
        GPBUtil::checkBool($var);
        $this->extract_support = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>bool score_support = 5;</code>
     * @return bool
     */
    public function getScoreSupport()
    {
        return $this->score_support;
    }

    /**
     * Generated from protobuf field <code>bool score_support = 5;</code>
     * @param bool $var
     * @return $this
     */
    public function setScoreSupport($var)
    {
        GPBUtil::checkBool($var);
        $this->score_support = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>bool attribute_support = 6;</code>
     * @return bool
     */
    public function getAttributeSupport()
    {
        return $this->attribute_support;
    }

    /**
     * Generated from protobuf field <code>bool attribute_support = 6;</code>
     * @param bool $var
     * @return $this
     */
    public function setAttributeSupport($var)
    {
        GPBUtil::checkBool($var);
        $this->attribute_support = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>.ScoreType score_type = 7;</code>
     * @return int
     */
    public function getScoreType()
    {
        return $this->score_type;
    }

    /**
     * Generated from protobuf field <code>.ScoreType score_type = 7;</code>
     * @param int $var
     * @return $this
     */
    public function setScoreType($var)
    {
        GPBUtil::checkEnum($var, \ScoreType::class);
        $this->score_type = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>float detection_threshold = 8;</code>
     * @return float
     */
    public function getDetectionThreshold()
    {
        return $this->detection_threshold;
    }

    /**
     * Generated from protobuf field <code>float detection_threshold = 8;</code>
     * @param float $var
     * @return $this
     */
    public function setDetectionThreshold($var)
    {
        GPBUtil::checkFloat($var);
        $this->detection_threshold = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>float match_threshold = 9;</code>
     * @return float
     */
    public function getMatchThreshold()
    {
        return $this->match_threshold;
    }

    /**
     * Generated from protobuf field <code>float match_threshold = 9;</code>
     * @param float $var
     * @return $this
     */
    public function setMatchThreshold($var)
    {
        GPBUtil::checkFloat($var);
        $this->match_threshold = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string algorithm = 10;</code>
     * @return string
     */
    public function getAlgorithm()
    {
        return $this->algorithm;
    }

    /**
     * Generated from protobuf field <code>string algorithm = 10;</code>
     * @param string $var
     * @return $this
     */
    public function setAlgorithm($var)
    {
        GPBUtil::checkString($var, True);
        $this->algorithm = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string notes = 11;</code>
     * @return string
     */
    public function getNotes()
    {
        return $this->notes;
    }

    /**
     * Generated from protobuf field <code>string notes = 11;</code>
     * @param string $var
     * @return $this
     */
    public function setNotes($var)
    {
        GPBUtil::checkString($var, True);
        $this->notes = $var;

        return $this;
    }

}

