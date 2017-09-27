# Go to https://developer.amazon.com

1. Sign up AWS.
2. Go AWS Lambda, create one, trigger "Alexa-skill" => lambda
3. Go Alexa skill, put your data, e.g. pizza topping, side dishes, ...
4. When you are building skill, You need Endpoint, select AWS Lambda ARN, type your lambda id.
- e.g. arn:aws:lambda:eu-west-1:383468313355:function:myTrafik




- Example of Service Simulator
{
  "session": {
    "new": true,
    "sessionId": "SessionId.b11f5939-3542-4cc0-875e-8aa390cfd826",
    "application": {
      "applicationId": "amzn1.ask.skill.6d6d69b3-2b2d-4696-8b50-19bbe4e9c08c"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AEW7K5IKBDHJ4KX57M7W2LTC7PY55KO3LPPBM2MP4OEJVOD2GRTDSXFVCTIUGSHEA234XY4PO3GKYDXKBDRUHCURYMLFJ5SYGCQJS3AMFNW22LXZ6APKCPN3KXKWKBUEL4XAHKQEUGXJK7PVHBQPO3MTCUWLE4GCDP3TU7ITK4TZ6FD635ANCSP2RZC4YMXH2W7GSETQFQNQNSQ"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.e60b1bf3-56c8-4f51-909a-0cc2c4128798",
    "intent": {
      "name": "StopIntent",
      "slots": {
        "Device": {
          "name": "Device"
        },
        "AlsoTrigger": {
          "name": "AlsoTrigger"
        },
        "Anaphor": {
          "name": "Anaphor"
        },
        "ApplicationDataSlot": {
          "name": "ApplicationDataSlot"
        },
        "ActiveUserTrigger": {
          "name": "ActiveUserTrigger"
        }
      }
    },
    "locale": "en-US",
    "timestamp": "2017-09-27T06:46:41Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.6d6d69b3-2b2d-4696-8b50-19bbe4e9c08c"
      },
      "user": {
        "userId": "amzn1.ask.account.AEW7K5IKBDHJ4KX57M7W2LTC7PY55KO3LPPBM2MP4OEJVOD2GRTDSXFVCTIUGSHEA234XY4PO3GKYDXKBDRUHCURYMLFJ5SYGCQJS3AMFNW22LXZ6APKCPN3KXKWKBUEL4XAHKQEUGXJK7PVHBQPO3MTCUWLE4GCDP3TU7ITK4TZ6FD635ANCSP2RZC4YMXH2W7GSETQFQNQNSQ"
      },
      "device": {
        "supportedInterfaces": {
          "Display": {
            "templateVersion": "1",
            "markupVersion": "1"
          }
        }
      }
    }
  },
  "version": "1.0"
}
