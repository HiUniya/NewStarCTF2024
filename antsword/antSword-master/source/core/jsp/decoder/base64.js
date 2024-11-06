/**
 * JSP::base64 解码器
 */

 'use strict';

 module.exports = {
   asoutput: (ext={}) => {
     /**
      * ext = {
      *   opts: 类型为 Object, Shell 配置
      * }
      */
     return `yv66vgAAADEAWQoADgAnCgAaACgJABoAKQgAKgoAKwAsCAAtCAAuCgAUAC8IADAKAAwAMQgAMgcAMwoADAA0BwA1CgA2ADcKAA4AOAgAOQcAOgoAFAA7BwA8CAA9CgAMAD4KAD8AQAgAQQcAQgcAQwEAA3JlcwEAEkxqYXZhL2xhbmcvU3RyaW5nOwEABjxpbml0PgEAFShMamF2YS9sYW5nL1N0cmluZzspVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBAAxCYXNlNjRFbmNvZGUBACYoTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvU3RyaW5nOwEACHRvU3RyaW5nAQAUKClMamF2YS9sYW5nL1N0cmluZzsBAApTb3VyY2VGaWxlAQATQXNvdXRwdXRCYXNlNjQuamF2YQwAHQBEDAAhACIMABsAHAEADGphdmEudmVyc2lvbgcARQwARgAiAQAAAQADMS45DABHAEgBABBqYXZhLnV0aWwuQmFzZTY0DABJAEoBAApnZXRFbmNvZGVyAQAPamF2YS9sYW5nL0NsYXNzDABLAEwBABBqYXZhL2xhbmcvT2JqZWN0BwBNDABOAE8MAFAAUQEADmVuY29kZVRvU3RyaW5nAQACW0IMAFIAUwEAEGphdmEvbGFuZy9TdHJpbmcBABZzdW4ubWlzYy5CQVNFNjRFbmNvZGVyDABUAFUHAFYMAFcAWAEABmVuY29kZQEAE2phdmEvbGFuZy9FeGNlcHRpb24BABJzcmMvQXNvdXRwdXRCYXNlNjQBAAMoKVYBABBqYXZhL2xhbmcvU3lzdGVtAQALZ2V0UHJvcGVydHkBAAljb21wYXJlVG8BABUoTGphdmEvbGFuZy9TdHJpbmc7KUkBAAdmb3JOYW1lAQAlKExqYXZhL2xhbmcvU3RyaW5nOylMamF2YS9sYW5nL0NsYXNzOwEACWdldE1ldGhvZAEAQChMamF2YS9sYW5nL1N0cmluZztbTGphdmEvbGFuZy9DbGFzczspTGphdmEvbGFuZy9yZWZsZWN0L01ldGhvZDsBABhqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2QBAAZpbnZva2UBADkoTGphdmEvbGFuZy9PYmplY3Q7W0xqYXZhL2xhbmcvT2JqZWN0OylMamF2YS9sYW5nL09iamVjdDsBAAhnZXRDbGFzcwEAEygpTGphdmEvbGFuZy9DbGFzczsBAAhnZXRCeXRlcwEABCgpW0IBABZnZXREZWNsYXJlZENvbnN0cnVjdG9yAQAzKFtMamF2YS9sYW5nL0NsYXNzOylMamF2YS9sYW5nL3JlZmxlY3QvQ29uc3RydWN0b3I7AQAdamF2YS9sYW5nL3JlZmxlY3QvQ29uc3RydWN0b3IBAAtuZXdJbnN0YW5jZQEAJyhbTGphdmEvbGFuZy9PYmplY3Q7KUxqYXZhL2xhbmcvT2JqZWN0OwAhABoADgAAAAEAAAAbABwAAAADAAEAHQAeAAEAHwAAAC4AAwACAAAADiq3AAEqKiu2AAK1AAOxAAAAAQAgAAAADgADAAAABAAEAAUADQAGAAEAIQAiAAEAHwAAAPAABgAGAAAAoBIEuAAFTRIGTiwSB7YACJsASxIJuAAKOgQZBBILA70ADLYADRkEA70ADrYADzoFGQW2ABASEQS9AAxZAxMAElO2AA0ZBQS9AA5ZAyu2ABNTtgAPwAAUTqcARBIVuAAKOgQZBAO9AAy2ABYDvQAOtgAXOgUZBbYAEBIYBL0ADFkDEwASU7YADRkFBL0ADlkDK7YAE1O2AA/AABROLbBOK7AAAQAGAJwAnQAZAAEAIAAAADYADQAAAAgABgAKAAkACwASAAwAGQANAC8ADgBXAA8AWgAQAGEAEQBzABIAmwAUAJ0AFQCeABYAAQAjACQAAQAfAAAAHQABAAEAAAAFKrQAA7AAAAABACAAAAAGAAEAAAAbAAEAJQAAAAIAJg==`;
   },
   decode_buff: (buff) => {
    return Buffer.from(buff.toString(), 'base64');
   }
 }