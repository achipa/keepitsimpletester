#include "extraspackage.h"

ExtrasPackage::ExtrasPackage(QObject* parent) :
    m_name(""),
    m_pname(""),
    m_version(""),
    m_karma(0),
    m_vote(0),
    m_status(false),
    m_installed(false),
    m_link(""),
    m_imageurl(""),
    m_waiting(QDateTime()),
    m_bugtracker("")
{
}

QString ExtrasPackage::toString()
{
    return QString("%0 (%1) %2, karma %3, my vote %4, unlock %5, since %6").arg(m_name).arg(m_pname).arg(m_version).arg(m_karma).arg(m_vote > 0 ? "GO" : m_vote < 0 ? "BLOCKER" : "none").arg(m_status ? "true" : "false" ).arg(m_waiting.toString());
}

