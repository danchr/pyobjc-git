from _objc import setSignatureForSelector

setSignatureForSelector("NSScanner", "scanCharactersFromSet:intoString:", "c@:@o^@")
setSignatureForSelector("NSScanner", "scanDouble:", "c@:o^d")
setSignatureForSelector("NSScanner", "scanFloat:", "c@:o^f")
setSignatureForSelector("NSScanner", "scanHexInt:", "c@:o^I")
setSignatureForSelector("NSScanner", "scanInt:", "c@:o^i")
setSignatureForSelector("NSScanner", "scanLongLong:", "c@:o^q")
setSignatureForSelector("NSScanner", "scanString:intoString:", "c@:@o^@")
setSignatureForSelector("NSScanner", "scanUpToCharactersFromSet:intoString:", "c@:@o^@")
setSignatureForSelector("NSScanner", "scanUpToString:intoString:", "c@:@o^@")
setSignatureForSelector("NSStream", "getStreamsToHost:port:inputStream:outputStream:", "v@:@io^@o^@")
setSignatureForSelector("NSString", "completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:", "I@:o^@co^@@")
setSignatureForSelector("NSString", "getLineStart:end:contentsEnd:forRange:", "v@:o^Io^Io^I{_NSRange=II}")
setSignatureForSelector("NSMutableAttributedString", "readFromURL:options:documentAttributes:", "c@:@@o^@")
setSignatureForSelector("NSAttributedString", "attribute:atIndex:effectiveRange:", "@0@4:8@12I16o^{_NSRange=II}20")
setSignatureForSelector("NSAttributedString", "attribute:atIndex:longestEffectiveRange:inRange:", "@0@4:8@12I16o^{_NSRange=II}20{_NSRange=II}24")
setSignatureForSelector("NSAttributedString", "attributesAtIndex:effectiveRange:", "@0@4:8I12o^{_NSRange=II}16")
setSignatureForSelector("NSAttributedString", "attributesAtIndex:longestEffectiveRange:inRange:", "@0@4:8I12o^{_NSRange=II}16{_NSRange=II}20")
setSignatureForSelector("NSAttributedString", "initWithHTML:baseURL:documentAttributes:", "@0@4:8@12@16o^@20")
setSignatureForSelector("NSAttributedString", "initWithHTML:documentAttributes:", "@@:@o^@")
setSignatureForSelector("NSAttributedString", "initWithPath:documentAttributes:", "@@:@o^@")
setSignatureForSelector("NSAttributedString", "initWithRTFDFileWrapper:documentAttributes:", "@@:@o^@")
setSignatureForSelector("NSAttributedString", "initWithRTFD:documentAttributes:", "@0@4:8@12o^@16")
setSignatureForSelector("NSAttributedString", "initWithRTF:documentAttributes:", "@0@4:8@12o^@16")
setSignatureForSelector("NSAttributedString", "initWithURL:documentAttributes:", "@0@4:8@12o^@16")
setSignatureForSelector("NSFileManager", "fileExistsAtPath:isDirectory:", "c0@4:8@12o^c16")
setSignatureForSelector("NSArray", "getObject:atIndex:", "c@:o^@I")
setSignatureForSelector("NSCalendarDate", "years:months:days:hours:minutes:seconds:sinceDate:", "v@:o^io^io^io^io^io^i@")
setSignatureForSelector("NSPropertyListSerialization", "dataFromPropertyList:format:errorDescription:", "@@:@io^@")
setSignatureForSelector("NSPropertyListSerialization", "propertyListFromData:mutabilityOption:format:errorDescription:", "@@:@iN^io^@")
setSignatureForSelector("NSAppleScript", "_initWithContentsOfFile:error:", "@@:@o^@")
setSignatureForSelector("NSAppleScript", "_initWithData:error:", "@@:@o^@")
setSignatureForSelector("NSAppleScript", "compileAndReturnError:", "c@:o^@")
setSignatureForSelector("NSAppleScript", "executeAndReturnError:", "@@:o^@")
setSignatureForSelector("NSAppleScript", "executeAppleEvent:error:", "@@:@o^@")
setSignatureForSelector("NSAppleScript", "initWithContentsOfURL:error:", "@@:@o^@")
setSignatureForSelector("NSFaultHandler", "extraData", "i@:")
setSignatureForSelector("NSFaultHandler", "setTargetClass:extraData:", "v@:#i")
setSignatureForSelector("NSFormatter", "getObjectValue:forString:errorDescription:", "c@:o^@@o^@")
setSignatureForSelector("NSFormatter", "isPartialStringValid:newEditingString:errorDescription:", "c@:@o^@o^@")
setSignatureForSelector("NSFormatter", "isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:", "c0@4:8o^@12o^{_NSRange=II}16@20{_NSRange=II}24o^@32")

setSignatureForSelector("NSObject", "validateValue:forKey:error:", "c@:N^@@o^@")
setSignatureForSelector("NSObject", "validateValue:forKeyPath:error:", "c@:N^@@o^@")
setSignatureForSelector("NSObject", "addObserver:forKeyPath:options:context:",
    "v@:@@Ii")
setSignatureForSelector("NSObject", "observeValueForKeyPath:ofObject:change:context:", "v@:@@@i")
setSignatureForSelector("NSArray", "addObserver:toObjectsAtIndexes:forKeyPath:options:context:", 'v@:@@@Ii')
setSignatureForSelector("NSURLConnection", "sendSynchronousRequest:returningResponse:error:", "@@:@o^@o^@")
setSignatureForSelector("NSString", "getParagraphStart:end:contentsEnd:forRange:", "v@:o^Io^Io^I{_NSRange=II}")
setSignatureForSelector("NSMutableAttributedString", "readFromData:options:documentAttributes:", "c@:@@o^@")
setSignatureForSelector("NSAttributedString", "initWithHTML:options:documentAttributes:", "@20@0:4@8@12o^@16")
setSignatureForSelector("NSAttributedString", "initWithDocFormat:documentAttributes:", "@@:@o^@")
setSignatureForSelector("NSKeyValueProperty", "keyPathIfAffectedByValueForKey:exactMatch:", "@@:@o^c")
setSignatureForSelector("NSKeyValueObservationForwarder", "initWithObserver:relationshipKey:keyPathFromRelatedObject:options:context:", "@@:@@@Ii")
setSignatureForSelector("NSDeserializer", "deserializePropertyListFromData:atCursor:mutableContainers:", "@@:@O^Ic")
setSignatureForSelector("NSDeserializer", "deserializePropertyListLazilyFromData:atCursor:length:mutableContainers:", "@@:@O^IIc")
setSignatureForSelector("OC_PythonObject", "addObserver:forKeyPath:options:context:", "v@:@@Ii")


# Technically incorrect, but not used anyway
setSignatureForSelector("NSObject", "setObservationInfo:", "v@:i")
setSignatureForSelector("NSObject", "observationInfo", "i@:")
