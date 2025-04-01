package de.stustapay.stustapay.ui.common

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Preview(showBackground = true)
@Composable
fun PreviewStatusText() {
    StatusText("roflcopter bla bla important message pls read me srsly gnampf")
}

@Composable
fun StatusText(
    status: String,
    modifier: Modifier = Modifier,
    scrollable: Boolean = true,
) {
    val scrollState = rememberScrollState()

    val mod = if (scrollable) {
        modifier
            .heightIn(min = 30.dp, max = 65.dp)
            .verticalScroll(scrollState)
    } else {
        modifier
    }
    Box(
        modifier = mod
            .fillMaxWidth()
    ) {
        Text(
            text = status,
            modifier = Modifier.fillMaxWidth(),
            style = MaterialTheme.typography.body1,
            fontFamily = FontFamily.Monospace,
        )
    }
}